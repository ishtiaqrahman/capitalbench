# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | xai-grok-4-3 | xai | 8 | -1.37% | -0.87% | -0.50% | 50.00% | 8.45% | -11.21% | -6.88% |
| 2 | anthropic-claude-opus-4-7 | anthropic | 8 | -1.39% | -0.87% | -0.52% | 50.00% | 8.48% | -11.35% | -6.88% |
| 3 | anthropic-claude-opus-4-8 | anthropic | 6 | -2.49% | -1.60% | -0.89% | 33.33% | 7.87% | -14.41% | -9.30% |
| 4 | openai-gpt-5-5 | openai | 8 | -2.83% | -0.87% | -1.96% | 37.50% | 9.92% | -21.75% | -6.88% |
| 5 | google-gemini-3-1-pro | google | 8 | -2.86% | -0.87% | -1.99% | 37.50% | 9.95% | -22.06% | -6.88% |

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

## Methodology

Official cumulative score: the public website averages CapitalBench Score across all completed rounds in the selected track. Models that did not participate in every resolved round are shown as short history until they build a full track history. CapitalBench Score compares the model return with the maximum possible return from the scored universe in that window.

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

- Round CB-2026-06-08-1W has no scored official or stability runs.
- Round CB-2026-06-09-1W has no scored official or stability runs.
- Round CB-2026-06-12-1W has no scored official or stability runs.
- Round CB-2026-06-13-1W has no scored official or stability runs.
