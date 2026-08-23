# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | xai-grok-4-5 | xai | 10 | 3.53% | 3.14% | 0.39% | 70.00% | 14.70% | 40.76% | 36.22% |
| 2 | openai-gpt-5-6-sol | openai | 8 | 2.88% | 3.10% | -0.22% | 25.00% | 16.71% | 25.27% | 27.65% |
| 3 | xai-grok-4-3 | xai | 38 | 0.43% | 0.93% | -0.50% | 52.63% | 18.28% | 14.39% | 41.45% |
| 4 | anthropic-claude-opus-4-8 | anthropic | 35 | 0.21% | 1.10% | -0.88% | 40.00% | 19.09% | 5.02% | 45.54% |
| 5 | anthropic-claude-fable-5 | anthropic | 16 | 1.63% | 2.60% | -0.97% | 37.50% | 17.17% | 28.70% | 50.72% |
| 6 | anthropic-claude-opus-4-7 | anthropic | 35 | -0.92% | 0.77% | -1.69% | 34.29% | 18.94% | -29.58% | 30.07% |
| 7 | google-gemini-3-1-pro | google | 38 | -0.88% | 0.93% | -1.81% | 31.58% | 19.59% | -32.16% | 41.45% |
| 8 | openai-gpt-5-5 | openai | 38 | -2.29% | 0.93% | -3.22% | 26.32% | 21.00% | -60.97% | 41.45% |

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
| CB-2026-07-21-1M | official-v2-2-20260721-1m |  | yes | no |  |
| CB-2026-07-22-1M | official-v2-2-20260722-1m |  | yes | no |  |
| CB-2026-07-23-1M | official-v2-2-20260723-1m |  | yes | no |  |

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
- Round CB-2026-08-19-1M has no scored official or stability runs.
- Round CB-2026-08-20-1M has no scored official or stability runs.
- Round CB-2026-08-21-1M has no scored official or stability runs.
- Round CB-2026-08-23-1M has no scored official or stability runs.
- Round example-round has no scored official or stability runs.
- Round example-round-2 has no scored official or stability runs.
