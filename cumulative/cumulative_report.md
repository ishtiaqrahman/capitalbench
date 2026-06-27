# CapitalBench Cumulative Results

## What This Is

Each round is a separate market decision with its own declared scoring window. Official results use one call per model. Stability results use repeated calls per model. Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. We do not backfill models into past official rounds. The official and stability leaderboards are separate, and there is no combined weighted score.

## Cumulative Official Leaderboard

| Rank | Model | Provider | Resolved Rounds | Avg Return | Avg S&P Return | Avg Alpha | Hit Rate vs S&P | Avg Regret | Cumulative Return | Cumulative S&P Return |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | anthropic-claude-fable-5 | anthropic | 3 | 2.13% | 1.23% | 0.90% | 66.67% | 8.90% | 6.47% | 3.73% |
| 2 | xai-grok-4-3 | xai | 20 | -0.16% | -0.64% | 0.48% | 55.00% | 9.39% | -4.35% | -12.22% |
| 3 | anthropic-claude-opus-4-7 | anthropic | 20 | -0.40% | -0.64% | 0.24% | 50.00% | 9.63% | -8.77% | -12.22% |
| 4 | anthropic-claude-opus-4-8 | anthropic | 15 | -0.89% | -0.84% | -0.05% | 40.00% | 9.20% | -13.11% | -12.03% |
| 5 | openai-gpt-5-5 | openai | 20 | -1.01% | -0.64% | -0.38% | 45.00% | 10.24% | -20.63% | -12.22% |
| 6 | google-gemini-3-1-pro | google | 20 | -1.28% | -0.64% | -0.64% | 45.00% | 10.51% | -24.36% | -12.22% |

## Cumulative Stability Leaderboard

_No rows._

## Round Index

| Round | Official Run | Stability Run | Official Included | Stability Included | Warnings |
| --- | --- | --- | --- | --- | --- |
| CB-2026-05-10-1M | official-round-1-clean |  | yes | no |  |
| CB-2026-05-17-1M | official-20260517 |  | yes | no |  |
| CB-2026-05-24-1M | official-20260524 |  | yes | no |  |
| CB-2026-05-24-1W | official-20260524-1W |  | yes | no |  |
| CB-2026-05-27-1W | official-20260527-1W |  | yes | no |  |
| CB-2026-05-28-1M | official-20260528-1M |  | yes | no |  |
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
- Round CB-2026-06-22-1M has no scored official or stability runs.
- Round CB-2026-06-22-1W has no scored official or stability runs.
- Round CB-2026-06-23-1M has no scored official or stability runs.
- Round CB-2026-06-23-1W has no scored official or stability runs.
- Round CB-2026-06-24-1M has no scored official or stability runs.
- Round CB-2026-06-24-1W has no scored official or stability runs.
- Round CB-2026-06-25-1M has no scored official or stability runs.
- Round CB-2026-06-25-1W has no scored official or stability runs.
- Round CB-2026-06-26-1M has no scored official or stability runs.
- Round CB-2026-06-26-1W has no scored official or stability runs.
- Round example-round has no scored official or stability runs.
- Round example-round-2 has no scored official or stability runs.
