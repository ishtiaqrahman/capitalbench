# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | xai-grok-4-3 | xai | 30 | -0.47% | 0.07% | -0.54% | 43.33% | 9.59% | -14.56% | 1.82% |
| 2 | anthropic-claude-opus-4-8 | anthropic | 28 | -0.65% | -0.02% | -0.64% | 32.14% | 9.55% | -17.65% | -0.82% |
| 3 | anthropic-claude-opus-4-7 | anthropic | 30 | -0.63% | 0.07% | -0.70% | 33.33% | 9.74% | -18.41% | 1.82% |
| 4 | anthropic-claude-fable-5 | anthropic | 10 | -0.52% | 0.44% | -0.97% | 30.00% | 10.92% | -5.47% | 4.48% |
| 5 | openai-gpt-5-5 | openai | 30 | -1.10% | 0.07% | -1.17% | 30.00% | 10.22% | -30.42% | 1.82% |
| 6 | google-gemini-3-1-pro | google | 30 | -1.21% | 0.07% | -1.28% | 33.33% | 10.33% | -32.63% | 1.82% |
| 7 | xai-grok-4-5 | xai | 3 | -2.82% | -0.14% | -2.69% | 33.33% | 14.24% | -8.45% | -0.43% |
| 8 | openai-gpt-5-6-sol | openai | 1 | -5.36% | -1.54% | -3.82% | 0.00% | 19.40% | -5.36% | -1.54% |

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

- Round CB-2026-07-13-1W has no scored official or stability runs.
- Round CB-2026-07-14-1W has no scored official or stability runs.
- Round CB-2026-07-15-1W has no scored official or stability runs.
- Round CB-2026-07-16-1W has no scored official or stability runs.
