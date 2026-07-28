# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | openai-gpt-5-6-sol | openai | 6 | 0.15% | -0.82% | 0.98% | 50.00% | 8.78% | 0.63% | -4.84% |
| 2 | xai-grok-4-5 | xai | 8 | 0.47% | -0.48% | 0.94% | 75.00% | 8.76% | 3.22% | -3.76% |
| 3 | xai-grok-4-3 | xai | 35 | 0.13% | -0.04% | 0.16% | 51.43% | 8.82% | 2.34% | -1.58% |
| 4 | anthropic-claude-fable-5 | anthropic | 15 | 0.11% | 0.07% | 0.04% | 53.33% | 9.46% | 1.25% | 0.98% |
| 5 | anthropic-claude-opus-4-8 | anthropic | 33 | -0.40% | -0.12% | -0.28% | 42.42% | 9.14% | -13.28% | -4.14% |
| 6 | anthropic-claude-opus-4-7 | anthropic | 35 | -0.45% | -0.04% | -0.41% | 42.86% | 9.39% | -15.83% | -1.58% |
| 7 | openai-gpt-5-5 | openai | 35 | -0.57% | -0.04% | -0.54% | 40.00% | 9.52% | -20.99% | -1.58% |
| 8 | google-gemini-3-1-pro | google | 35 | -0.63% | -0.04% | -0.59% | 42.86% | 9.57% | -22.38% | -1.58% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-24-1W | official-20260524-1W |  | yes | no |  |
| CB-2026-05-27-1W | official-20260527-1W |  | yes | no |  |
| CB-2026-05-28-1W | official-20260528-1W |  | yes | no |  |
| CB-2026-05-29-1W | official-20260529-1W |  | yes | no |  |
| CB-2026-06-01-1W | official-20260601 |  | yes | no |  |
| CB-2026-06-02-1W | official-20260602-clean |  | yes | no |  |
| CB-2026-06-03-1W | official-20260603 |  | yes | no |  |
| CB-2026-06-05-1W | official-20260605 |  | yes | no |  |
| CB-2026-06-08-1W | official-20260608 |  | yes | no |  |
| CB-2026-06-09-1W | official-20260609 |  | yes | no |  |
| CB-2026-06-12-1W | official-20260612-clean |  | yes | no |  |
| CB-2026-06-13-1W | official-20260613 |  | yes | no |  |
| CB-2026-06-15-1W | official-20260615-no-fable |  | yes | no |  |
| CB-2026-06-16-1W | official-20260616-no-fable |  | yes | no |  |
| CB-2026-06-17-1W | official-20260617-no-fable |  | yes | no |  |
| CB-2026-06-18-1W | official-20260618-no-fable |  | yes | no |  |
| CB-2026-06-22-1W | official-20260622-no-fable |  | yes | no |  |
| CB-2026-06-23-1W | official-20260623-no-fable |  | yes | no |  |
| CB-2026-06-24-1W | official-20260624-no-fable |  | yes | no |  |
| CB-2026-06-25-1W | official-20260625-no-fable |  | yes | no |  |
| CB-2026-06-26-1W | official-20260626-no-fable |  | yes | no |  |
| CB-2026-06-29-1W | official-20260629-no-fable |  | yes | no |  |
| CB-2026-06-30-1W | official-20260630-no-fable-clean |  | yes | no |  |
| CB-2026-07-01-1W | official-20260701-with-fable |  | yes | no |  |
| CB-2026-07-02-1W | official-20260702 |  | yes | no |  |
| CB-2026-07-06-1W | official-20260706 |  | yes | no |  |
| CB-2026-07-07-1W | official-20260707 |  | yes | no |  |
| CB-2026-07-08-1W | official-20260708 |  | yes | no |  |
| CB-2026-07-09-1W | official-20260709 |  | yes | no |  |
| CB-2026-07-10-1W | official-20260710 |  | yes | no |  |
| CB-2026-07-13-1W | official-20260713 |  | yes | no |  |
| CB-2026-07-14-1W | official-20260714 |  | yes | no |  |
| CB-2026-07-15-1W | official-20260715 |  | yes | no |  |
| CB-2026-07-17-1W | official-v2-all-weekly-final-20260717 |  | yes | no |  |
| CB-2026-07-20-1W | official-v2-20260720 |  | yes | no |  |

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

- Round CB-2026-07-16-1W has no scored official or stability runs.
- Round CB-2026-07-21-1W has no scored official or stability runs.
- Round CB-2026-07-22-1W has no scored official or stability runs.
- Round CB-2026-07-23-1W has no scored official or stability runs.
- Round CB-2026-07-24-1W has no scored official or stability runs.
- Round CB-2026-07-27-1W has no scored official or stability runs.
