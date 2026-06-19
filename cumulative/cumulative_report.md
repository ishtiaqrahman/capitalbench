# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | xai-grok-4-3 | xai | 2 | -0.48% | -0.71% | 0.22% | 50.00% | 11.32% | -0.98% | -1.41% |
| 2 | anthropic-claude-opus-4-7 | anthropic | 2 | -0.82% | -0.71% | -0.12% | 50.00% | 11.66% | -1.66% | -1.41% |
| 3 | google-gemini-3-1-pro | google | 2 | -2.11% | -0.71% | -1.40% | 50.00% | 12.94% | -4.25% | -1.41% |
| 4 | openai-gpt-5-5 | openai | 2 | -3.92% | -0.71% | -3.21% | 50.00% | 14.75% | -7.90% | -1.41% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-10-1M | official-round-1-clean |  | yes | no |  |
| CB-2026-05-17-1M | official-20260517 |  | yes | no |  |

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

- Round CB-2026-05-24-1M has no scored official or stability runs.
- Round CB-2026-05-28-1M has no scored official or stability runs.
- Round CB-2026-05-29-1M has no scored official or stability runs.
- Round CB-2026-06-01-1M has no scored official or stability runs.
- Round CB-2026-06-02-1M has no scored official or stability runs.
- Round CB-2026-06-03-1M has no scored official or stability runs.
- Round CB-2026-06-05-1M has no scored official or stability runs.
- Round CB-2026-06-08-1M has no scored official or stability runs.
- Round CB-2026-06-09-1M has no scored official or stability runs.
- Round CB-2026-06-12-1M has no scored official or stability runs.
- Round CB-2026-06-13-1M has no scored official or stability runs.
- Round CB-2026-06-15-1M has no scored official or stability runs.
- Round CB-2026-06-16-1M has no scored official or stability runs.
- Round CB-2026-06-17-1M has no scored official or stability runs.
- Round CB-2026-06-18-1M has no scored official or stability runs.
- Round example-round has no scored official or stability runs.
- Round example-round-2 has no scored official or stability runs.
