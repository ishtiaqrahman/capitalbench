# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | anthropic-claude-opus-4-7 | anthropic | 9 | -1.04% | -0.54% | -0.50% | 44.44% | 8.88% | -9.78% | -4.91% |
| 2 | xai-grok-4-3 | xai | 9 | -1.28% | -0.54% | -0.74% | 44.44% | 9.12% | -11.70% | -4.91% |
| 3 | anthropic-claude-opus-4-8 | anthropic | 7 | -2.12% | -1.07% | -1.04% | 28.57% | 8.71% | -14.28% | -7.38% |
| 4 | openai-gpt-5-5 | openai | 9 | -2.58% | -0.54% | -2.04% | 33.33% | 10.43% | -22.22% | -4.91% |
| 5 | google-gemini-3-1-pro | google | 9 | -2.70% | -0.54% | -2.16% | 33.33% | 10.54% | -23.12% | -4.91% |

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

- Round CB-2026-06-09-1W has no scored official or stability runs.
- Round CB-2026-06-12-1W has no scored official or stability runs.
- Round CB-2026-06-13-1W has no scored official or stability runs.
- Round CB-2026-06-15-1W has no scored official or stability runs.
