# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | openai-gpt-5-6-sol | openai | 5 | 3.35% | 3.26% | 0.09% | 40.00% | 11.90% | 17.72% | 17.38% |
| 2 | xai-grok-4-3 | xai | 35 | 0.08% | 0.77% | -0.69% | 48.57% | 17.94% | 0.32% | 30.07% |
| 3 | xai-grok-4-5 | xai | 7 | 2.44% | 3.27% | -0.83% | 57.14% | 12.12% | 17.89% | 25.26% |
| 4 | anthropic-claude-opus-4-8 | anthropic | 32 | -0.31% | 0.93% | -1.24% | 34.38% | 18.91% | -11.11% | 33.83% |
| 5 | anthropic-claude-fable-5 | anthropic | 13 | 1.05% | 2.55% | -1.50% | 30.77% | 15.90% | 14.06% | 38.60% |
| 6 | anthropic-claude-opus-4-7 | anthropic | 35 | -0.92% | 0.77% | -1.69% | 34.29% | 18.94% | -29.58% | 30.07% |
| 7 | google-gemini-3-1-pro | google | 35 | -1.54% | 0.77% | -2.32% | 25.71% | 19.57% | -44.51% | 30.07% |
| 8 | openai-gpt-5-5 | openai | 35 | -2.92% | 0.77% | -3.69% | 20.00% | 20.94% | -66.40% | 30.07% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-10-1M | official-round-1-clean |  | yes | no |  |
| CB-2026-05-17-1M | official-20260517 |  | yes | no |  |
| CB-2026-05-24-1M | official-20260524 |  | yes | no |  |
| CB-2026-05-28-1M | official-20260528-1M |  | yes | no |  |
| CB-2026-05-29-1M | official-20260529-1M |  | yes | no |  |
| CB-2026-06-01-1M | official-20260601 |  | yes | no |  |
| CB-2026-06-02-1M | official-20260602 |  | yes | no |  |
| CB-2026-06-03-1M | official-20260603 |  | yes | no |  |
| CB-2026-06-05-1M | official-20260605-r3 |  | yes | no |  |
| CB-2026-06-08-1M | official-20260608 |  | yes | no |  |
| CB-2026-06-09-1M | official-20260609 |  | yes | no |  |
| CB-2026-06-12-1M | official-20260612 |  | yes | no |  |
| CB-2026-06-13-1M | official-20260613-no-fable |  | yes | no |  |
| CB-2026-06-15-1M | official-20260615-no-fable |  | yes | no |  |
| CB-2026-06-16-1M | official-20260616-no-fable |  | yes | no |  |
| CB-2026-06-17-1M | official-20260617-no-fable |  | yes | no |  |
| CB-2026-06-18-1M | official-20260618-no-fable |  | yes | no |  |
| CB-2026-06-22-1M | official-20260622-no-fable |  | yes | no |  |
| CB-2026-06-23-1M | official-20260623-no-fable |  | yes | no |  |
| CB-2026-06-24-1M | official-20260624-no-fable |  | yes | no |  |
| CB-2026-06-25-1M | official-20260625-no-fable |  | yes | no |  |
| CB-2026-06-26-1M | official-20260626-no-fable |  | yes | no |  |
| CB-2026-06-29-1M | official-20260629-no-fable-clean |  | yes | no |  |
| CB-2026-06-30-1M | official-20260630-no-fable-clean |  | yes | no |  |
| CB-2026-07-01-1M | official-20260701-with-fable |  | yes | no |  |
| CB-2026-07-02-1M | official-20260702 |  | yes | no |  |
| CB-2026-07-06-1M | official-20260706 |  | yes | no |  |
| CB-2026-07-07-1M | official-20260707 |  | yes | no |  |
| CB-2026-07-08-1M | official-20260708 |  | yes | no |  |
| CB-2026-07-09-1M | official-20260709 |  | yes | no |  |
| CB-2026-07-10-1M | official-20260710 |  | yes | no |  |
| CB-2026-07-13-1M | official-20260713 |  | yes | no |  |
| CB-2026-07-14-1M | official-20260714 |  | yes | no |  |
| CB-2026-07-15-1M | official-20260715 |  | yes | no |  |
| CB-2026-07-17-1M | official-v2-all-final-20260717 |  | yes | no |  |

## Methodology

Official cumulative score: the public website divides summed model returns by summed oracle returns across all completed rounds in the selected track. Models that did not participate in every resolved round are shown as short history until they build a full track history. A score of 100 matches the hindsight oracle, 0 means no net return, and negative values preserve losses.

Stability cumulative score: For each model, we average its repeated-run alpha and consistency across the rounds where each model participated.

The CSV cumulative official leaderboard keeps average alpha versus the S&P 500 as supporting context for compatibility; the website scorecard is the primary benchmark view.

The cumulative stability leaderboard is sorted by average repeated-run alpha versus the S&P 500 across the rounds where each model participated.

The official leaderboard measures the saved public model decision. The stability leaderboard measures consistency under repeated calls. They are not combined.

## Limitations

- A small number of rounds may be noisy.
- Short-window market returns are noisy.
- Models can win by luck.
- This is not financial advice.
- Provider costs and hidden reasoning tokens may not be directly comparable.
- Only resolved rounds are included.

## Warnings

- Round CB-2026-07-16-1M has no scored official or stability runs.
- Round CB-2026-07-21-1M has no scored official or stability runs.
- Round CB-2026-07-22-1M has no scored official or stability runs.
- Round CB-2026-07-23-1M has no scored official or stability runs.
- Round CB-2026-07-24-1M has no scored official or stability runs.
- Round CB-2026-07-27-1M has no scored official or stability runs.
- Round CB-2026-07-28-1M has no scored official or stability runs.
- Round CB-2026-07-29-1M has no scored official or stability runs.
- Round CB-2026-07-30-1M has no scored official or stability runs.
- Round CB-2026-07-31-1M has no scored official or stability runs.
- Round CB-2026-08-04-1M has no scored official or stability runs.
- Round CB-2026-08-05-1M has no scored official or stability runs.
- Round CB-2026-08-07-1M has no scored official or stability runs.
- Round CB-2026-08-09-1M has no scored official or stability runs.
- Round CB-2026-08-11-1M has no scored official or stability runs.
- Round CB-2026-08-13-1M has no scored official or stability runs.
- Round CB-2026-08-15-1M has no scored official or stability runs.
- Round CB-2026-08-18-1M has no scored official or stability runs.
- Round example-round has no scored official or stability runs.
- Round example-round-2 has no scored official or stability runs.
