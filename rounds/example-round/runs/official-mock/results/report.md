# CapitalBench Report: example-round / official-mock

## Official One-Shot Leaderboard

This is the official CapitalBench score for this run.

_This run used mock execution and is not a public benchmark result._

## Round Summary

- Run ID: official-mock
- Run type: official
- Replicates: 1
- Mock: yes
- Title: Example CapitalBench Round
- Description: Fake one-month allocation round for testing the CapitalBench protocol.
- Decision date: 2026-04-30
- Decision deadline: 2026-04-30T20:00:00Z
- Horizon: One month
- Entry date: 2026-05-01
- Exit date: 2026-06-01
- Entry rule: Use the closing prices in prices/entry_prices.csv as the investable entry point.
- Exit rule: Use the closing prices in prices/exit_prices.csv as the realized exit point.
- Options: 40

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
| ENERGY | Energy Sector | 95.0 | 101.65 | 0.07000000000000006 | 1 |
| SEMICONDUCTORS | Semiconductors | 230.0 | 246.1 | 0.07000000000000006 | 1 |
| TECHNOLOGY | Technology Sector | 210.0 | 221.55 | 0.05500000000000016 | 3 |
| NASDAQ100 | Nasdaq 100 | 420.0 | 441.0 | 0.050000000000000044 | 4 |
| MOMENTUM | US Momentum Equities | 190.0 | 199.5 | 0.050000000000000044 | 4 |
| GOLD | Gold | 44.0 | 46.2 | 0.050000000000000044 | 4 |
| LARGE_GROWTH | US Large-Cap Growth | 360.0 | 377.28 | 0.04799999999999982 | 7 |
| FINANCIALS | Financials Sector | 55.0 | 57.2 | 0.040000000000000036 | 8 |
| INDIA | India Equities | 56.0 | 58.24 | 0.040000000000000036 | 8 |
| SOFTWARE | Software | 88.0 | 91.52 | 0.040000000000000036 | 8 |
| LARGE_VALUE | US Large-Cap Value | 180.0 | 185.4 | 0.030000000000000027 | 11 |
| INDUSTRIALS | Industrials Sector | 130.0 | 133.9 | 0.030000000000000027 | 11 |
| DEVELOPED_EX_US | Developed Markets ex-US | 51.0 | 52.53 | 0.030000000000000027 | 11 |
| EUROPE | Europe Equities | 68.0 | 70.04 | 0.030000000000000027 | 11 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 185.0 | 189.63 | 0.02502702702702697 | 15 |
| COMMUNICATIONS | Communication Services Sector | 86.0 | 88.15 | 0.025000000000000133 | 16 |
| TOTAL_US_MARKET | Total US Stock Market | 260.0 | 266.24 | 0.02400000000000002 | 17 |
| SP500 | S&P 500 | 500.0 | 510.0 | 0.020000000000000018 | 18 |
| DIVIDEND | US Dividend Equities | 78.0 | 79.56 | 0.020000000000000018 | 18 |
| MATERIALS | Materials Sector | 92.0 | 93.84 | 0.020000000000000018 | 18 |
| UTILITIES | Utilities Sector | 70.0 | 71.4 | 0.020000000000000018 | 18 |
| BROAD_COMMODITIES | Broad Commodities | 14.0 | 14.28 | 0.020000000000000018 | 18 |
| MID_CAP | US Mid-Cap Stocks | 275.0 | 279.13 | 0.01501818181818182 | 23 |
| JAPAN | Japan Equities | 72.0 | 73.08 | 0.014999999999999902 | 24 |
| LOW_VOL | US Low Volatility Equities | 66.0 | 66.66 | 0.010000000000000009 | 25 |
| HEALTHCARE | Healthcare Sector | 150.0 | 151.5 | 0.010000000000000009 | 25 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.0 | 78.78 | 0.010000000000000009 | 25 |
| TIPS | Treasury Inflation-Protected Securities | 107.0 | 107.54 | 0.005046728971962677 | 28 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.0 | 91.32 | 0.0035164835164833708 | 29 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.0 | 98.1 | 0.0010204081632652073 | 30 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 31 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.0 | 93.53 | -0.0050000000000000044 | 32 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.0 | 108.13 | -0.007981651376146814 | 33 |
| SMALL_CAP | US Small-Cap Stocks | 210.0 | 207.9 | -0.010000000000000009 | 34 |
| SMALL_VALUE | US Small-Cap Value | 165.0 | 163.35 | -0.010000000000000009 | 34 |
| CONSUMER_STAPLES | Consumer Staples Sector | 78.0 | 77.22 | -0.010000000000000009 | 34 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 90.0 | 88.2 | -0.020000000000000018 | 37 |
| REAL_ESTATE | Real Estate Sector | 42.0 | 40.95 | -0.02499999999999991 | 38 |
| EMERGING_MARKETS | Emerging Markets | 46.0 | 44.85 | -0.025000000000000022 | 38 |
| CHINA | China Equities | 48.0 | 45.6 | -0.04999999999999993 | 40 |

## Leaderboard

Official One-Shot Leaderboard

| model_id | selected_option_id | confidence | selected_asset_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-example | FINANCIALS | 0.58 | 0.040000000000000036 | 0.020000000000000018 | 0.030000000000000027 | 8 | True | True |
| anthropic-example | INDUSTRIALS | 0.66 | 0.030000000000000027 | 0.010000000000000009 | 0.040000000000000036 | 11 | True | True |
| google-example | UTILITIES | 0.5 | 0.020000000000000018 | 0.0 | 0.050000000000000044 | 18 | False | True |
| openai-example | SHORT_TREASURY | 0.66 | 0.0035164835164833708 | -0.016483516483516647 | 0.06648351648351669 | 29 | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 5469b9d5c6ae1ef00391d3a0f402672cd9ffcef2daed440b98838afab868569a |
| options.yaml | 451c26dbfd8a498bef50df205d8c7489acf8edde5c48c21e132bda42e47cf056 |
| prompt.md | 812ad113dd6b8806da33c76cbe7d4300ef9e5970e1179050f5755ff0b6c9c21f |
| manifest.yaml | d4012521232401b751577821c546137582d74ae05d9fb7086a4016afcd447a72 |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses one selected option per model.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Scores evaluate a single selected option and do not model portfolio allocation.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
