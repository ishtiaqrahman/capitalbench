# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | xai-grok-4-3 | xai | 7 | -1.66% | -1.08% | -0.58% | 42.86% | 7.94% | -11.80% | -7.41% |
| 2 | anthropic-claude-opus-4-7 | anthropic | 7 | -1.72% | -1.08% | -0.64% | 42.86% | 8.00% | -12.14% | -7.41% |
| 3 | anthropic-claude-opus-4-8 | anthropic | 5 | -3.16% | -2.04% | -1.13% | 20.00% | 7.07% | -15.14% | -9.81% |
| 4 | openai-gpt-5-5 | openai | 7 | -2.97% | -1.08% | -1.89% | 42.86% | 9.25% | -20.25% | -7.41% |
| 5 | google-gemini-3-1-pro | google | 7 | -3.29% | -1.08% | -2.21% | 42.86% | 9.57% | -22.16% | -7.41% |

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

- Round CB-2026-06-05-1W has no scored official or stability runs.
- Round CB-2026-06-08-1W has no scored official or stability runs.
- Round CB-2026-06-09-1W has no scored official or stability runs.
- Round CB-2026-06-12-1W has no scored official or stability runs.
