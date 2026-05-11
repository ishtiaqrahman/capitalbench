# CapitalBench Report: example-round-2 / official-mock

## Official One-Shot Leaderboard

This is the official CapitalBench score for this run.

_This run used mock execution and is not a public benchmark result._

## Round Summary

- Run ID: official-mock
- Run type: official
- Replicates: 1
- Mock: yes
- Title: Example CapitalBench Round 2
- Description: Fake second one-month allocation round for testing the CapitalBench protocol.
- Decision date: 2026-04-30
- Decision deadline: 2026-04-30T20:00:00Z
- Horizon: One month
- Entry date: 2026-05-01
- Exit date: 2026-06-01
- Entry rule: Use the closing prices in prices/entry_prices.csv as the investable entry point.
- Exit rule: Use the closing prices in prices/exit_prices.csv as the realized exit point.
- Options: 12

## Model Decisions

| model_id | provider | selected_option_id | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- |
| xai-example | xai | FINANCIALS | 0.58 | Mock dry-run selected FINANCIALS deterministically for xai-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| anthropic-example | anthropic | INDUSTRIALS | 0.66 | Mock dry-run selected INDUSTRIALS deterministically for anthropic-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| google-example | google | UTILITIES | 0.5 | Mock dry-run selected UTILITIES deterministically for google-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| openai-example | openai | SHORT_TREASURY | 0.66 | Mock dry-run selected SHORT_TREASURY deterministically for openai-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ENERGY | Energy | 95.0 | 101.65 | 0.07000000000000006 | 1 |
| NASDAQ100 | Nasdaq 100 | 420.0 | 441.0 | 0.050000000000000044 | 2 |
| FINANCIALS | Financials | 55.0 | 57.2 | 0.040000000000000036 | 3 |
| VALUE | US Value | 180.0 | 185.4 | 0.030000000000000027 | 4 |
| INDUSTRIALS | Industrials | 130.0 | 133.9 | 0.030000000000000027 | 4 |
| SP500 | S&P 500 | 500.0 | 510.0 | 0.020000000000000018 | 6 |
| UTILITIES | Utilities | 70.0 | 71.4 | 0.020000000000000018 | 6 |
| HEALTHCARE | Healthcare | 150.0 | 151.5 | 0.010000000000000009 | 8 |
| SHORT_TREASURY | Short Treasury Bills | 91.0 | 91.32 | 0.0035164835164833708 | 9 |
| CASH | Cash |  |  | 0.0 | 10 |
| SMALL_CAP | US Small Cap | 210.0 | 207.9 | -0.010000000000000009 | 11 |
| LONG_BONDS | Long Treasury Bonds | 90.0 | 88.2 | -0.020000000000000018 | 12 |

## Leaderboard

Official One-Shot Leaderboard

| model_id | selected_option_id | confidence | selected_asset_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-example | FINANCIALS | 0.58 | 0.040000000000000036 | 0.020000000000000018 | 0.030000000000000027 | 3 | True | True |
| anthropic-example | INDUSTRIALS | 0.66 | 0.030000000000000027 | 0.010000000000000009 | 0.040000000000000036 | 4 | True | True |
| google-example | UTILITIES | 0.5 | 0.020000000000000018 | 0.0 | 0.050000000000000044 | 6 | False | True |
| openai-example | SHORT_TREASURY | 0.66 | 0.0035164835164833708 | -0.016483516483516647 | 0.06648351648351669 | 9 | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: no

| file | sha256 |
| --- | --- |
| briefing.md | 5469b9d5c6ae1ef00391d3a0f402672cd9ffcef2daed440b98838afab868569a |
| options.yaml | 2874422adb8ce5d6624189692b7c2928cf62ab3a6a130699eac008a0c821791c |
| prompt.md | 812ad113dd6b8806da33c76cbe7d4300ef9e5970e1179050f5755ff0b6c9c21f |
| manifest.yaml | 99c2e542b9f1005b5885b8d54b624506f3e43ed0c44de07315f642fafd51d108 |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses one selected option per model.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Scores evaluate a single selected option and do not model portfolio allocation.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
