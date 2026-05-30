# CapitalBench Cumulative Results

## What This Is

Each round is a separate one-month market decision. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | openai-gpt-5-5 | openai | 1 | 5.09% | 1.45% | 3.63% | 100.00% | 7.99% | 5.09% | 1.45% |
| 2 | xai-grok-4-3 | xai | 1 | 3.69% | 1.45% | 2.24% | 100.00% | 9.38% | 3.69% | 1.45% |
| 3 | anthropic-claude-opus-4-7 | anthropic | 1 | 3.11% | 1.45% | 1.66% | 100.00% | 9.96% | 3.11% | 1.45% |
| 4 | google-gemini-3-1-pro | google | 1 | 2.79% | 1.45% | 1.34% | 100.00% | 10.28% | 2.79% | 1.45% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-24-1W | official-20260524-1W |  | yes | no |  |

## Methodology

Official cumulative score: For each model, we average its official one-shot alpha versus the S&P 500 across the rounds where each model participated.

Stability cumulative score: For each model, we average its repeated-run alpha and consistency across the rounds where each model participated.

The cumulative official leaderboard is sorted by average alpha versus the S&P 500 across the rounds where each model participated.

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

- Round CB-2026-05-27-1W has no scored official or stability runs.
- Round CB-2026-05-28-1W has no scored official or stability runs.
- Round CB-2026-05-29-1W has no scored official or stability runs.
