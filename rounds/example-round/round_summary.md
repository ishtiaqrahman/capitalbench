# CapitalBench Round Summary: example-round

## Round Overview

- Title: Example CapitalBench Round
- Description: Fake one-month allocation round for testing the CapitalBench protocol.
- Decision deadline: 2026-04-30T20:00:00Z
- Horizon: One month
- Entry rule: Use the closing prices in prices/entry_prices.csv as the investable entry point.
- Exit rule: Use the closing prices in prices/exit_prices.csv as the realized exit point.
- Official run ID: official-mock
- Stability run ID: stability-mock

## Result Types

The official leaderboard and stability analysis are separate. The official leaderboard is the one-shot score. Stability measures repeated-call consistency. CapitalBench does not create a combined weighted score.

## Official One-Shot Leaderboard

| model_id | selected_option_id | selected_asset_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options |
| --- | --- | --- | --- | --- | --- |
| xai-example | FINANCIALS | 0.040000000000000036 | 0.020000000000000018 | 0.030000000000000027 | 8 |
| anthropic-example | INDUSTRIALS | 0.030000000000000027 | 0.010000000000000009 | 0.040000000000000036 | 11 |
| google-example | UTILITIES | 0.020000000000000018 | 0.0 | 0.050000000000000044 | 18 |
| openai-example | SHORT_TREASURY | 0.0035164835164833708 | -0.016483516483516647 | 0.06648351648351669 | 29 |

## Multi-Run Stability Analysis

| model_id | pick_distribution | modal_pick | consistency_rate | average_repeated_return | average_repeated_alpha_vs_sp500 | best_replicate_option_id | worst_replicate_option_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-example | {"INDUSTRIALS": 5} | INDUSTRIALS | 1.0 | 0.030000000000000027 | 0.010000000000000009 | INDUSTRIALS | INDUSTRIALS |
| google-example | {"UTILITIES": 5} | UTILITIES | 1.0 | 0.020000000000000018 | 0.0 | UTILITIES | UTILITIES |
| openai-example | {"SHORT_TREASURY": 5} | SHORT_TREASURY | 1.0 | 0.0035164835164833708 | -0.016483516483516647 | SHORT_TREASURY | SHORT_TREASURY |
| xai-example | {"FINANCIALS": 5} | FINANCIALS | 1.0 | 0.040000000000000036 | 0.020000000000000018 | FINANCIALS | FINANCIALS |

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 5469b9d5c6ae1ef00391d3a0f402672cd9ffcef2daed440b98838afab868569a |
| options.yaml | 451c26dbfd8a498bef50df205d8c7489acf8edde5c48c21e132bda42e47cf056 |
| prompt.md | 812ad113dd6b8806da33c76cbe7d4300ef9e5970e1179050f5755ff0b6c9c21f |
| manifest.yaml | d4012521232401b751577821c546137582d74ae05d9fb7086a4016afcd447a72 |

## Limitations

- The official score uses exactly one scored decision per model.
- Stability analysis is secondary and does not change the official leaderboard.
- Prices are loaded from local CSV files and are not fetched live.
- Scores evaluate one selected option, not a portfolio.
