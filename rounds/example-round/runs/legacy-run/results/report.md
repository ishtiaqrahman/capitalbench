# CapitalBench Report: example-round / legacy-run

## Round Summary

- Run ID: legacy-run
- Title: Example CapitalBench Round
- Description: Fake one-month allocation round for testing the CapitalBench protocol.
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
| gpt-example | openai | ENERGY | 0.64 | Energy has the best upside in the fake briefing because supply conditions are tight and risk appetite is still present. | Oil prices could reverse quickly; Sector concentration creates idiosyncratic risk |
| gemini-example | google | NASDAQ100 | 0.61 | Large-cap growth momentum looks strongest in the fake setup and could outperform over one month. | Technology valuations may compress; A defensive rotation could hurt QQQ |
| xai-example | xai | FINANCIALS | 0.58 | Mock dry-run selected FINANCIALS deterministically for xai-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| anthropic-example | anthropic | INDUSTRIALS | 0.66 | Mock dry-run selected INDUSTRIALS deterministically for anthropic-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| claude-example | anthropic | VALUE | 0.58 | Value balances equity participation with less dependence on large-cap growth momentum. | Growth leadership could continue; Financial conditions could tighten further |
| google-example | google | UTILITIES | 0.5 | Mock dry-run selected UTILITIES deterministically for google-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| openai-example | openai | SHORT_TREASURY | 0.66 | Mock dry-run selected SHORT_TREASURY deterministically for openai-example. | Mock output is not a real model decision; Dry-run data must not be interpreted as benchmark evidence |
| grok-example | xai | SHORT_TREASURY | 0.55 | Short Treasury exposure is the conservative choice if sticky inflation pressures risk assets. | Equities could rally sharply; Cash-like exposure limits upside |

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

| model_id | selected_option_id | confidence | selected_asset_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-example | ENERGY | 0.64 | 0.07000000000000006 | 0.050000000000000044 | 0.0 | 1 | True | True |
| gemini-example | NASDAQ100 | 0.61 | 0.050000000000000044 | 0.030000000000000027 | 0.020000000000000018 | 2 | True | True |
| xai-example | FINANCIALS | 0.58 | 0.040000000000000036 | 0.020000000000000018 | 0.030000000000000027 | 3 | True | True |
| anthropic-example | INDUSTRIALS | 0.66 | 0.030000000000000027 | 0.010000000000000009 | 0.040000000000000036 | 4 | True | True |
| claude-example | VALUE | 0.58 | 0.030000000000000027 | 0.010000000000000009 | 0.040000000000000036 | 4 | True | True |
| google-example | UTILITIES | 0.5 | 0.020000000000000018 | 0.0 | 0.050000000000000044 | 6 | False | True |
| openai-example | SHORT_TREASURY | 0.66 | 0.0035164835164833708 | -0.016483516483516647 | 0.06648351648351669 | 9 | False | True |
| grok-example | SHORT_TREASURY | 0.55 | 0.0035164835164833708 | -0.016483516483516647 | 0.06648351648351669 | 9 | False | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| gpt-example | ENERGY | 0.050000000000000044 | 0.042 | 1.1904761904761914 |
| gemini-example | NASDAQ100 | 0.030000000000000027 | 0.028 | 1.0714285714285723 |
| claude-example | VALUE | 0.010000000000000009 | 0.036 | 0.27777777777777807 |
| grok-example | SHORT_TREASURY | -0.016483516483516647 | 0.031 | -0.5317263381779563 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 5469b9d5c6ae1ef00391d3a0f402672cd9ffcef2daed440b98838afab868569a |
| options.yaml | 2874422adb8ce5d6624189692b7c2928cf62ab3a6a130699eac008a0c821791c |
| prompt.md | 812ad113dd6b8806da33c76cbe7d4300ef9e5970e1179050f5755ff0b6c9c21f |
| manifest.yaml | d4012521232401b751577821c546137582d74ae05d9fb7086a4016afcd447a72 |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Provider adapters define the interface but do not call model APIs yet.
- Scores evaluate a single selected option and do not model portfolio allocation.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
