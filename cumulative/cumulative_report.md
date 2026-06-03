# CapitalBench Cumulative Results

## What This Is

Each round is a separate one-month market decision. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | openai-gpt-5-5 | openai | 2 | 5.29% | 1.33% | 3.97% | 100.00% | 6.93% | 10.86% | 2.67% |
| 2 | xai-grok-4-3 | xai | 2 | 4.37% | 1.33% | 3.05% | 100.00% | 7.84% | 8.93% | 2.67% |
| 3 | google-gemini-3-1-pro | google | 2 | 4.03% | 1.33% | 2.70% | 100.00% | 8.19% | 8.20% | 2.67% |
| 4 | anthropic-claude-opus-4-7 | anthropic | 2 | 4.01% | 1.33% | 2.68% | 100.00% | 8.21% | 8.17% | 2.67% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-24-1W | official-20260524-1W |  | yes | no |  |
| CB-2026-05-27-1W | official-20260527-1W |  | yes | no |  |

## Methodology

Official cumulative score: For each model, the public website averages CapitalBench Score across completed rounds where each model participated. CapitalBench Score compares the model return with the maximum possible return from the scored universe in that window.

Stability cumulative score: For each model, we average its repeated-run alpha and consistency across the rounds where each model participated.

The CSV cumulative official leaderboard keeps average alpha versus the S&P 500 as supporting context for compatibility; the website scorecard is the primary benchmark view.

The cumulative stability leaderboard is sorted by average repeated-run alpha versus the S&P 500 across the rounds where each model participated.

The official leaderboard measures one-shot decision quality. The stability leaderboard measures consistency under repeated calls. They are not combined.

## Limitations

- A small number of rounds may be noisy.
- One-month market returns are noisy.
- Models can win by luck.
- This is not financial advice.
- Provider costs and hidden reasoning tokens may not be directly comparable.
- Only resolved rounds are included.

## Warnings

- Round CB-2026-05-28-1W has no scored official or stability runs.
- Round CB-2026-05-29-1W has no scored official or stability runs.
- Round CB-2026-06-01-1W has no scored official or stability runs.
- Round CB-2026-06-02-1W has no scored official or stability runs.
- Round CB-2026-06-03-1W has no scored official or stability runs.
