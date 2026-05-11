# CapitalBench Report: example-round-2 / stability-mock

## Multi-Run Stability Analysis

This is not the official leaderboard. It measures decision stability under repeated calls.

- Replicate count: 5
- Mock: yes

## Round Summary

- Run ID: stability-mock
- Run type: stability
- Title: Example CapitalBench Round 2
- Decision deadline: 2026-04-30T20:00:00Z
- Horizon: One month
- Entry rule: Use the closing prices in prices/entry_prices.csv as the investable entry point.
- Exit rule: Use the closing prices in prices/exit_prices.csv as the realized exit point.
- Options: 12

## All Repeated Picks

| model_id | replicate_index | selected_option_id | selected_asset_return | alpha_vs_sp500 | cost_usd |
| --- | --- | --- | --- | --- | --- |
| anthropic-example | 1 | INDUSTRIALS | 0.030000000000000027 | 0.010000000000000009 |  |
| anthropic-example | 2 | INDUSTRIALS | 0.030000000000000027 | 0.010000000000000009 |  |
| anthropic-example | 3 | INDUSTRIALS | 0.030000000000000027 | 0.010000000000000009 |  |
| anthropic-example | 4 | INDUSTRIALS | 0.030000000000000027 | 0.010000000000000009 |  |
| anthropic-example | 5 | INDUSTRIALS | 0.030000000000000027 | 0.010000000000000009 |  |
| google-example | 1 | UTILITIES | 0.020000000000000018 | 0.0 |  |
| google-example | 2 | UTILITIES | 0.020000000000000018 | 0.0 |  |
| google-example | 3 | UTILITIES | 0.020000000000000018 | 0.0 |  |
| google-example | 4 | UTILITIES | 0.020000000000000018 | 0.0 |  |
| google-example | 5 | UTILITIES | 0.020000000000000018 | 0.0 |  |
| openai-example | 1 | SHORT_TREASURY | 0.0035164835164833708 | -0.016483516483516647 |  |
| openai-example | 2 | SHORT_TREASURY | 0.0035164835164833708 | -0.016483516483516647 |  |
| openai-example | 3 | SHORT_TREASURY | 0.0035164835164833708 | -0.016483516483516647 |  |
| openai-example | 4 | SHORT_TREASURY | 0.0035164835164833708 | -0.016483516483516647 |  |
| openai-example | 5 | SHORT_TREASURY | 0.0035164835164833708 | -0.016483516483516647 |  |
| xai-example | 1 | FINANCIALS | 0.040000000000000036 | 0.020000000000000018 |  |
| xai-example | 2 | FINANCIALS | 0.040000000000000036 | 0.020000000000000018 |  |
| xai-example | 3 | FINANCIALS | 0.040000000000000036 | 0.020000000000000018 |  |
| xai-example | 4 | FINANCIALS | 0.040000000000000036 | 0.020000000000000018 |  |
| xai-example | 5 | FINANCIALS | 0.040000000000000036 | 0.020000000000000018 |  |

## Stability Table

| model_id | provider | valid_replicates | invalid_replicates | pick_distribution | modal_pick | consistency_rate | average_repeated_return | average_repeated_alpha_vs_sp500 | best_replicate_option_id | best_replicate_return | worst_replicate_option_id | worst_replicate_return | total_cost_usd | average_cost_usd | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-example | anthropic | 5 | 0 | {"INDUSTRIALS": 5} | INDUSTRIALS | 1.0 | 0.030000000000000027 | 0.010000000000000009 | INDUSTRIALS | 0.030000000000000027 | INDUSTRIALS | 0.030000000000000027 |  |  |  |
| google-example | google | 5 | 0 | {"UTILITIES": 5} | UTILITIES | 1.0 | 0.020000000000000018 | 0.0 | UTILITIES | 0.020000000000000018 | UTILITIES | 0.020000000000000018 |  |  |  |
| openai-example | openai | 5 | 0 | {"SHORT_TREASURY": 5} | SHORT_TREASURY | 1.0 | 0.0035164835164833708 | -0.016483516483516647 | SHORT_TREASURY | 0.0035164835164833708 | SHORT_TREASURY | 0.0035164835164833708 |  |  |  |
| xai-example | xai | 5 | 0 | {"FINANCIALS": 5} | FINANCIALS | 1.0 | 0.040000000000000036 | 0.020000000000000018 | FINANCIALS | 0.040000000000000036 | FINANCIALS | 0.040000000000000036 |  |  |  |

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

- Stability analysis is secondary and does not replace the official one-shot leaderboard.
- Repeated calls use the same prompt, briefing, and options, but provider systems may still vary internally.
- Prices are loaded from local CSV files and are not fetched live.
- Scores evaluate a single selected option and do not model portfolio allocation.
