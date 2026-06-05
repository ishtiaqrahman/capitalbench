# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | openai-gpt-5-5 | openai | 3 | 4.35% | 0.99% | 3.36% | 100.00% | 5.33% | 13.60% | 3.01% |
| 2 | anthropic-claude-opus-4-8 | anthropic | 1 | 3.58% | 0.33% | 3.25% | 100.00% | 1.04% | 3.58% | 0.33% |
| 3 | google-gemini-3-1-pro | google | 3 | 4.00% | 0.99% | 3.00% | 100.00% | 5.69% | 12.46% | 3.01% |
| 4 | xai-grok-4-3 | xai | 3 | 3.78% | 0.99% | 2.79% | 100.00% | 5.90% | 11.77% | 3.01% |
| 5 | anthropic-claude-opus-4-7 | anthropic | 3 | 3.64% | 0.99% | 2.65% | 100.00% | 6.04% | 11.32% | 3.01% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-24-1W | official-20260524-1W |  | yes | no |  |
| CB-2026-05-27-1W | official-20260527-1W |  | yes | no |  |
| CB-2026-05-28-1W | official-20260528-1W |  | yes | no |  |

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

- Round CB-2026-05-29-1W has no scored official or stability runs.
- Round CB-2026-06-01-1W has no scored official or stability runs.
- Round CB-2026-06-02-1W has no scored official or stability runs.
- Round CB-2026-06-03-1W has no scored official or stability runs.
