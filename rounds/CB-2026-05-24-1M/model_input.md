# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make one-shot market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

Optimize only for the portfolio you expect to perform best from the entry price to the exit date, approximately one month later. Do not optimize for long-term attractiveness beyond this scoring window.

Your objective is to allocate 100% across the allowed options to maximize expected one-month realized portfolio return, measured from the entry date to the exit date, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official one-shot leaderboard.

Your portfolio is scored by the weighted realized percentage return over the one-month round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

You may use your internal learned knowledge and general market priors. Do not browse, use tools, request updated market data, use external retrieval, or intentionally rely on facts, market prices, news, or events dated after the research cutoff. If your internal knowledge conflicts with the briefing, prioritize the briefing.

You must allocate exactly 100% across allowed options. Use only the holding count, allocation increment, minimum allocation, and cash or benchmark constraints stated in the round metadata. Do not short, use leverage, or choose an option outside the allowed option list.

Return only valid JSON. Do not include markdown, prose, citations, or commentary outside the JSON.

Required JSON format:

{
  "round_id": "<round_id>",
  "model_id": "<model_id>",
  "provider": "<provider>",
  "mode": "closed_capability",
  "portfolio": [
    {
      "option_id": "<one allowed option ID>",
      "allocation_pct": <integer percentage>,
      "rationale": "<brief holding-level rationale>"
    }
  ],
  "confidence": <number from 0 to 1>,
  "portfolio_rationale": "<1-3 sentence allocation rationale>",
  "rationale_summary": "<1-3 sentence rationale>",
  "key_risks": [
    "<risk 1>",
    "<risk 2>"
  ]
}

Rules:
- portfolio must contain only IDs from the allowed option list.
- allocation_pct values must be integers in the stated allocation increment.
- allocation_pct values must sum to exactly 100.
- confidence must be between 0 and 1.
- confidence should reflect your confidence that this is the best portfolio decision under the round constraints.
- portfolio_rationale and rationale_summary are required and should be concise.
- key_risks must be a list of 2-5 concrete risks that could cause the portfolio to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup portfolio, second-best portfolio, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.

## Round Metadata

- Round ID: CB-2026-05-24-1M
- Decision date: 2026-05-24
- Research cutoff UTC: 2026-05-24T21:34:31Z
- Decision deadline UTC: 2026-05-25T01:00:00Z
- Horizon: one month
- Entry date: 2026-05-22
- Exit date: 2026-06-24
- Scoring window: 2026-05-22 to 2026-06-24; optimize for this one month window only.
- Entry rule: Use adjusted close from the last trading close before the decision deadline; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on the exit_date for each selected option; CASH return is 0 unless explicitly priced.
- Submission format: portfolio
- Scoring benchmark: S&P 500 / SPY
- Return calculation: adjusted close prices are used when available.
- Portfolio holdings allowed: 1-5
- Portfolio allocation increment: 5%
- Portfolio minimum allocation: 5%
- Portfolio total allocation: 100%

## Briefing

# CapitalBench Briefing

## 1. Fact-Only Statement

This briefing contains factual inputs only. It does not rank, recommend, analyze, or map facts to CapitalBench options.

## 2. Full-Universe Trailing Returns

# Full-Universe Trailing Returns

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-05-24
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-05-24 | 0.00% | 0.00% | 0.00% | 0.00% | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-05-22 | 0.07% | 0.27% | 1.79% | 3.87% | pass |
| SP500 | SPY | us_broad_market | 2026-05-22 | 0.88% | 4.44% | 12.14% | 30.23% | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-05-22 | 1.12% | 4.19% | 12.28% | 30.20% | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-05-22 | 1.21% | 8.08% | 18.87% | 41.58% | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-05-22 | 0.51% | 4.35% | 7.10% | 28.49% | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-05-22 | 1.78% | 3.81% | 16.57% | 29.11% | pass |
| MID_CAP | IJH | us_size_factor | 2026-05-22 | 1.77% | 0.98% | 14.96% | 25.04% | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-05-22 | 2.71% | 3.06% | 19.46% | 42.27% | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-05-22 | 2.59% | 2.10% | 21.13% | 44.43% | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-05-22 | 3.50% | 5.22% | 24.08% | 31.70% | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-05-22 | 2.61% | 0.63% | 4.05% | 4.38% | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-05-22 | 1.79% | 8.08% | 25.75% | 35.58% | pass |
| TECHNOLOGY | XLK | us_sector | 2026-05-22 | 2.34% | 12.59% | 29.34% | 59.97% | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-05-22 | -0.53% | -0.07% | 2.82% | 16.66% | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-05-22 | 2.27% | 0.41% | 4.72% | 14.04% | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-05-22 | 0.19% | 1.89% | 11.64% | 6.80% | pass |
| HEALTHCARE | XLV | us_sector | 2026-05-22 | 3.30% | 3.96% | -2.65% | 17.05% | pass |
| FINANCIALS | XLF | us_sector | 2026-05-22 | 1.64% | 1.01% | 0.95% | 5.37% | pass |
| INDUSTRIALS | XLI | us_sector | 2026-05-22 | 0.22% | -0.41% | 15.22% | 23.60% | pass |
| ENERGY | XLE | us_sector | 2026-05-22 | 0.08% | 4.61% | 35.43% | 49.78% | pass |
| MATERIALS | XLB | us_sector | 2026-05-22 | -0.02% | -3.14% | 17.36% | 19.64% | pass |
| UTILITIES | XLU | us_sector | 2026-05-22 | 3.37% | -1.80% | 3.21% | 15.05% | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-05-22 | 3.08% | 1.67% | 10.70% | 13.43% | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-05-22 | 0.40% | -1.43% | -1.70% | 4.01% | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-05-22 | 1.22% | -1.98% | -3.80% | 4.71% | pass |
| TIPS | TIP | bonds_and_rates | 2026-05-22 | -0.21% | -0.77% | 0.48% | 4.59% | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-05-22 | 0.47% | -0.74% | -0.44% | 6.66% | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-05-22 | 0.57% | -0.19% | 2.10% | 7.29% | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-05-22 | 0.43% | -0.82% | -0.24% | 5.30% | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-05-22 | 2.00% | 3.40% | 19.50% | 32.10% | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-05-22 | 0.92% | -0.07% | 12.16% | 26.81% | pass |
| EUROPE | VGK | international_equity | 2026-05-22 | 3.11% | 1.62% | 13.73% | 19.88% | pass |
| JAPAN | EWJ | international_equity | 2026-05-22 | 0.59% | 4.91% | 16.32% | 31.24% | pass |
| CHINA | MCHI | international_equity | 2026-05-22 | -1.94% | -3.93% | -9.26% | 3.63% | pass |
| INDIA | INDA | international_equity | 2026-05-22 | 0.83% | -2.40% | -10.75% | -11.34% | pass |
| GOLD | IAU | commodities | 2026-05-22 | -0.82% | -4.44% | 8.95% | 33.81% | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-05-22 | -2.20% | 2.30% | 40.29% | 46.95% | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-05-22 | 3.59% | 13.80% | 70.47% | 143.47% | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-05-22 | 2.43% | 10.34% | -8.04% | -7.77% | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-05-22 | 2.49% | 2.25% | 11.66% | 20.48% | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-05-22 | 0.74% | -1.22% | 10.46% | 67.17% | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-05-22 | 3.58% | 0.70% | 13.85% | 26.09% | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-05-22 | 3.73% | 4.43% | 12.37% | 32.46% | pass |
| CANADA | EWC | country_equity | 2026-05-22 | 1.86% | 0.98% | 15.64% | 33.73% | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-05-22 | 3.34% | 0.21% | 14.51% | 22.83% | pass |
| AUSTRALIA | EWA | country_equity | 2026-05-22 | 0.21% | -1.34% | 15.07% | 15.87% | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-05-22 | 1.77% | 17.77% | 106.17% | 215.76% | pass |
| TAIWAN | EWT | country_equity | 2026-05-22 | 6.09% | 9.93% | 62.06% | 89.28% | pass |
| BRAZIL | EWZ | country_equity | 2026-05-22 | 0.39% | -8.94% | 17.01% | 38.74% | pass |
| MEXICO | EWW | country_equity | 2026-05-22 | 0.71% | -0.90% | 19.12% | 33.03% | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-05-22 | -0.07% | -3.99% | 7.77% | 36.80% | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-05-22 | 0.55% | -0.86% | 0.47% | 6.90% | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-05-22 | 0.05% | -0.85% | 0.64% | 5.66% | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-05-22 | 0.49% | -0.65% | 1.32% | 11.38% | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-05-22 | 1.03% | 0.01% | 0.10% | 2.26% | pass |
| SILVER | SLV | commodities | 2026-05-22 | -0.98% | -0.63% | 46.60% | 124.50% | pass |
| COPPER | CPER | commodities | 2026-05-22 | 2.05% | 5.36% | 25.10% | 28.07% | pass |
| AGRICULTURE | DBA | commodities | 2026-05-22 | -0.97% | 0.62% | 11.19% | 5.21% | pass |
| OIL | USO | commodities | 2026-05-22 | -4.93% | 6.44% | 100.11% | 107.27% | pass |
| US_DOLLAR | UUP | currencies | 2026-05-22 | 0.00% | 1.06% | 1.16% | 4.93% | pass |
| EURO | FXE | currencies | 2026-05-22 | -0.14% | -0.93% | 1.06% | 2.87% | pass |
| YEN | FXY | currencies | 2026-05-22 | -0.26% | 0.23% | -1.64% | -10.79% | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-05-22 | -4.15% | -2.41% | -15.05% | -30.52% | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-05-22 | -7.10% | -11.13% | -30.65% | -19.66% | pass |

## 3. Macro Snapshot

### Core Macro Table

| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Inflation | CPI | 3.80% | 3.3% | prior value (YoY) | Apr 2026 | May 12, 2026 | source 1 |
| Inflation | CPI | 0.60% | 0.90% | prior value (MoM) | Apr 2026 | May 12, 2026 | source 2 |
| Inflation | Core CPI | 2.8% | 2.6% | prior value (YoY) | Apr 2026 | May 13, 2026 | source 1 |
| Inflation | Core CPI | 0.4% | 0.2% | prior value (MoM) | Apr 2026 | May 13, 2026 | source 5 |
| Inflation | PCE Price Index | 3.50% | 2.8% | prior value (YoY) | Mar 2026 | Apr 30, 2026 | source 7 |
| Inflation | PCE Price Index | 0.9% | 0.6% | prior value (MoM) | Mar 2026 | Apr 30, 2026 | source 8 |
| Inflation | Core PCE Price Index | 3.20% | 3.0% | prior value (YoY) | Mar 2026 | Apr 30, 2026 | source 9 |
| Inflation | Core PCE Price Index | 0.30% | 0.40% | prior value (MoM) | Mar 2026 | Apr 30, 2026 | source 11 |
| Inflation | PPI Final Demand | 1.4% | 0.7% | prior value (MoM) | Apr 2026 | May 13, 2026 | source 12 |
| Inflation | PPI Final Demand | 6.0% | not source-reported | not source-reported | Apr 2026 | May 13, 2026 | source 13 |
| Labor | Unemployment Rate | 4.3% | 4.3% | prior value | Apr 2026 | May 8, 2026 | source 15 |
| Labor | Nonfarm Payrolls | 115,000 | not source-reported | not source-reported | Apr 2026 | May 8, 2026 | source 4 |
| Labor | Average Hourly Earnings | 3.60% | 3.40% | prior value (YoY) | Apr 2026 | May 12, 2026 | source 17 |
| Labor | Average Hourly Earnings | 0.20% | not source-reported | not source-reported | Apr 2026 | May 12, 2026 | source 18 |
| Labor | Weekly Jobless Claims | 209,000 | 212,000 | prior value | Week ending May 16, 2026 | May 21, 2026 | source 20 |
| Growth | Real GDP | 2.0% | 0.5% | prior value (Advance Q1) | Q1 2026 | Apr 30, 2026 | source 22 |
| Consumption | Retail Sales | 0.50% | 1.6% | revision / prior value (MoM) | Apr 2026 | May 14, 2026 | source 24 |
| Consumption | Personal Spending | 0.9% | 0.6% | prior value (MoM) | Mar 2026 | Apr 30, 2026 | source 8 |
| Production | Industrial Production | 0.70% | -0.3% | prior value (MoM) | Apr 2026 | May 15, 2026 | source 27 |
| Business Activity | ISM Manufacturing PMI | 52.7% | 52.7% | prior value | Apr 2026 | May 1, 2026 | source 29 |
| Business Activity | ISM Services PMI | 53.6 | 54.0 | prior value | Apr 2026 | May 5, 2026 | source 31 |
| Sentiment | Consumer Sentiment | 44.8 | 49.8 | prior value | May 2026 | May 22, 2026 | source 33 |
| Housing | Housing Starts | 1,465,000 | 1,507,000 | revision / prior value | Apr 2026 | May 21, 2026 | source 35 |
| Housing | Building Permits | 1,442,000 | 1,363,000 | prior value | Apr 2026 | May 21, 2026 | source 36 |
| Housing | Existing Home Sales | 4,020,000 | 4,010,000 | prior value | Apr 2026 | May 11, 2026 | source 38 |

### Rates, Credit, Liquidity, And Volatility

| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Policy Rates | Federal Funds Target Range | 3.50% - 3.75% | not source-reported | not source-reported | May 2026 | Mar 18, 2026 | source 59 |
| Policy Rates | Latest FOMC Decision | Unchanged | not source-reported | not source-reported | May 2026 | Mar 18, 2026 | source 59 |
| Policy Rates | Market-Implied Rate Expectation (June) | 95.9% probability of hold | 100% | revision / prior expectation | June 2026 | May 5, 2026 | source 62 |
| Yields | 3-Month Treasury Yield | 3.68% | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 64 |
| Yields | 2-Year Treasury Yield | 4.13% | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 64 |
| Yields | 10-Year Treasury Yield | 4.56% | 4.57% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 64 |
| Yields | 30-Year Treasury Yield | 5.07% | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 64 |
| Yields | 10-Year Real Yield (DFII10) | 2.18% | not source-reported | not source-reported | May 21, 2026 | May 22, 2026 | source 67 |
| Yields | 10-Year Breakeven Inflation | 2.39% | not source-reported | not source-reported | May 21, 2026 | May 21, 2026 | source 68 |
| Yields | Yield Curve Spread (10Y vs 3M) | +0.89% (89 bp) | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 64 |
| Yields | Yield Curve Spread (10Y vs 2Y) | +0.43% (43 bp) | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 64 |
| Currency | US Dollar Index (DXY) | 99.3240 | +0.07% | prior value (1 day) | May 22, 2026 | May 24, 2026 | source 69 |
| Volatility | VIX | 16.70 | -0.03 | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 70 |
| Volatility | MOVE Index | 78.43 | -0.31 | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 70 |
| Credit | Investment-Grade Credit Spread (BBB) | 0.33% | 0.33% | prior value (1 day) | May 21, 2026 | May 22, 2026 | source 71 |
| Credit | High-Yield Credit Spread | 2.78% | 2.80% | prior value (1 day) | May 21, 2026 | May 22, 2026 | source 72 |
| Liquidity | Financial Conditions Index (NFCI) | -0.52 | -0.50 | prior value (1 week) | Apr 24, 2026 | May 20, 2026 | source 73 |
| Liquidity | Money-Market Fund Assets | $7.77 trillion | $7.75 trillion | prior value (1 week) | May 20, 2026 | May 21, 2026 | source 75 |

### Commodity And Currency State

| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Commodities | WTI Crude | 96.60 USD | +0.26% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 95 |
| Commodities | Brent Crude | 104.25 USD | +0.69% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 97 |
| Commodities | Natural Gas | 2.92 USD | +0.48% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 97 |
| Commodities | Gold | 4,530.30 USD | +0.21% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 97 |
| Commodities | Silver | 76.04 USD | +0.19% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 97 |
| Commodities | Copper | 6.35 USD | +0.05% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 97 |
| Commodities | Broad Commodity Index (S&P GSCI) | 731.68 | -0.01% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 100 |
| Commodities | Broad Commodity Index (BCOM) | 138.6635 | -0.18% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 102 |
| Currency | US Dollar Index (DXY) | 99.3240 | +0.07% | prior value (1 day) | May 22, 2026 | May 22, 2026 | source 69 |
| Currency | Euro (EUR/USD) | 1.1570 | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 103 |
| Currency | Yen (USD/JPY) | 159.183 | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | source 104 |

## 4. Asset-Group Context

| asset_group | covered_options_or_area | fact_type | factual_statement | source_reported_comparison | comparison_type | date_or_period | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cash and short-duration Treasuries | US interest rates | policy_or_regulatory_fact | The Federal Open Market Committee paused the federal funds target rate at a range of 3.5% to 3.75%, with four formal dissents. | 3.5% to 3.75% | prior value | May 2026 | source 1 |
| cash and short-duration Treasuries | FOMC dissent metrics | observed_value | The May 2026 Federal Reserve rate decision recorded four formal dissenting votes, the highest number of dissents in a single FOMC meeting since late 1992. | most dissents in a meeting since late 1992 | explicit range or percentile | May 2026 | source 1 |
| intermediate Treasuries | US 10-year yield | observed_value | The 10-year US Treasury yield closed the weekly trading session at 4.570%, compared with a 52-week high of 4.668% earlier in the same week. | 4.668% | explicit range or percentile | May 22, 2026 | source 9 |
| broad US equities | US CPI inflation | observed_value | The US headline annual inflation rate was 3.8%, and energy prices were up 17.9% year over year. | 3.3% | prior value | April 2026 | source 5 |
| broad US equities | S&P 500 valuation | observed_value | The S&P 500 Shiller Cyclically Adjusted Price-to-Earnings ratio recorded a level of 41.6. | second-highest measurement in over 140 years | explicit range or percentile | May 2026 | source 14 |
| semiconductors | corporate revenue growth | observed_value | Nvidia Corporation reported Q1 FY2027 aggregate revenue of $81.6 billion and Data Center revenue of $75.0 billion. | +85% | year-over-year change | Q1 FY2027 | source 15 |
| Europe | ECB interest rates | policy_or_regulatory_fact | The European Central Bank Governing Council maintained its deposit facility rate at 2.00% and revised its baseline 2026 headline inflation forecast to 1.9%. | 2.00% | prior value | April 30, 2026 | source 35 |
| UK | BoE interest rates | policy_or_regulatory_fact | The Bank of England's Monetary Policy Committee voted 8 to 1 to maintain the official Bank Rate at 3.75%. | 3.75% | consensus / forecast comparison | April 30, 2026 | source 38 |
| Japan | BoJ interest rates | policy_or_regulatory_fact | The Bank of Japan maintained its short-term policy rate at 0.75%; three board members formally indicated preference for a rate increase. | 0.75% | prior value | April 28, 2026 | source 41 |
| Canada | BoC interest rates | policy_or_regulatory_fact | The Bank of Canada held its overnight target rate at 2.25%. | 2.25% | consensus / forecast comparison | April 29, 2026 | source 44 |
| South Africa | SARB interest rates | policy_or_regulatory_fact | The South African Reserve Bank kept the benchmark repurchase rate at 6.75%. | 6.75% | prior value | March 26, 2026 | source 50 |
| South Africa | domestic CPI | observed_value | South African headline consumer inflation was 4.0%; the source reported a R3.06 per litre rise in petrol prices. | 3.1% | prior value | April 2026 | source 51 |
| Brazil | Copom interest rates | policy_or_regulatory_fact | The Banco Central do Brasil lowered the Selic target rate to 14.50% and projected inflation at 4.6% for 2026 and 3.5% for 2027. | 14.75% | prior value | April 29, 2026 | source 47 |
| Mexico | Banxico interest rates | policy_or_regulatory_fact | The Bank of Mexico lowered its benchmark interest rate by 25 basis points to 6.50%. | 6.75% | prior value | May 7, 2026 | source 49 |
| China | manufacturing PMI | observed_value | The RatingDog China General Manufacturing PMI was 52.2. | 50.8 | prior value | April 2026 | source 54 |
| India | GDP growth forecast | labeled_forecast_or_estimate | The United Nations' economic growth projection for India in fiscal 2026-27 was 6.4%. | 7.5% | prior value | FY2026-27 | source 55 |
| Taiwan | GDP expansion | observed_value | Taiwan's economy expanded by 13.7% in the first quarter, and exports increased 35.3% year over year. | 13.7% | year-over-year change | Q1 2026 | source 57 |
| credit | corporate bond spreads | observed_value | The ICE BofA US Corporate Bond Spread for investment-grade credit measured 0.75%, while the high-yield spread registered at 2.78%. | not source-reported | not source-reported | May 21, 2026 | source 12 |
| real estate | pending home sales | observed_value | US pending home sales rose 1.4% to an index level of 74.8. | +1.0% | consensus / forecast comparison | April 2026 | source 19 |
| real estate | housing inventory | observed_value | Unsold US housing inventory was 1.47 million units, equal to 4.4 months of supply. | 4.2 months | prior value | April 2026 | source 22 |
| consumer discretionary | advance retail sales | observed_value | US advance retail and food services sales totaled $757.1 billion, a 0.5% monthly increase. | +4.9% | year-over-year change | April 2026 | source 23 |
| regional banks | sector performance | observed_value | The S&P Regional Banks Index generated an 8.45% total return year-to-date; total assets for insured commercial banks and savings institutions were $25.3 trillion. | 8.45% | year-to-date change | May 1, 2026 | source 25 |
| aerospace/defense | defense budget request | policy_or_regulatory_fact | The White House proposed a $1.5 trillion defense budget for fiscal year 2027, including $1.1 trillion in base discretionary funding. | $1 trillion | prior value | FY2027 | source 27 |
| utilities | sector M&A activity | scheduled_event | NextEra Energy and Dominion Energy announced a $67 billion all-stock combination agreement. | not source-reported | not source-reported | May 18, 2026 | source 29 |
| biotech | ETF valuation metrics | observed_value | The State Street SPDR S&P Biotech ETF (XBI), comprising 143 holdings, reported an aggregate Price/Earnings Ratio FY1 of 18.92 and a Price/Cash Flow ratio of 17.74. | not source-reported | not source-reported | May 21, 2026 | source 32 |
| gold | price forecast revision | labeled_forecast_or_estimate | J.P. Morgan research lowered its 2026 average gold price forecast to $5,243 per ounce. | $5,708/oz | revision | 2026 | source 66 |
| silver | physical supply balance | labeled_forecast_or_estimate | The Silver Institute's World Silver Survey projected a 67 million ounce supply deficit for 2026 and projected physical investment demand of 227 million ounces. | 20% | year-over-year change | 2026 | source 5 |
| copper | spot pricing | observed_value | Copper prices traded at $6.35 USD per pound. | +31.38% | year-over-year change | May 22, 2026 | source 67 |
| oil | OPEC+ supply policy | policy_or_regulatory_fact | Seven OPEC+ participating countries announced a collective production adjustment of 188 thousand barrels per day starting the following month. | not source-reported | not source-reported | June 2026 | source 59 |
| oil | OPEC membership changes | policy_or_regulatory_fact | The United Arab Emirates formally withdrew from the OPEC and OPEC+ alliances. | not source-reported | not source-reported | May 1, 2026 | source 61 |
| bitcoin ETF | fund capital flows | observed_value | Bitcoin ETFs recorded daily capital redemptions of $100.9 million. | $648.6 million | prior value | May 2026 | source 71 |
| ethereum ETF | fund capital flows | observed_value | Ethereum ETFs recorded daily capital redemptions of $32.6 million. | not source-reported | not source-reported | May 2026 | source 71 |

## 5. Tension Ledger

| area | source_reported_fact_1 | source_reported_fact_2 | unresolved_item | source_or_sources |
| --- | --- | --- | --- | --- |
| Inflation and labor | CPI YoY increased to 3.8% in April 2026. | Nonfarm Payrolls increased by 115,000, and unemployment was 4.3%. | Subsequent employment data alongside reported inflation data were not provided. | source 16 |
| Consumer sentiment and spending | Michigan Consumer Sentiment Index was 44.8 in May 2026. | Retail Sales increased 0.5% and Personal Spending increased 0.9% month-over-month. | Subsequent consumer spending data after the reported sentiment observation were not provided. | source 8 |
| Manufacturing input costs and employment | ISM Manufacturing Prices Index was 84.6%. | ISM Manufacturing Employment Index was 46.4%. | Later manufacturing employment and price-index observations were not provided. | source 29 |
| Services prices and new orders | ISM Services Prices Index was 70.7% in April 2026. | ISM Services New Orders Index fell 7.1 percentage points to 53.5%. | Later services prices and new-orders observations were not provided. | source 32 |
| Energy prices and commodity indices | WTI crude oil was $96.60 and Brent crude was $104.25. | S&P GSCI Total Return Index had a 1-day change of -0.01% and month-to-date change of -4.78%. | Later broad commodity index observations were not provided. | source 95 |
| Housing inventory and financing costs | US housing inventory was 1.47 million units, equal to 4.4 months of supply. | Mortgage borrowing costs were reported above 6% on average. | The aggregate transaction-volume effect was not source-reported. | source 20 |
| FOMC rate setting | The Federal Reserve held the target rate steady at 3.5% to 3.75%. | Four policymakers formally dissented, the most dissents since late 1992. | The trajectory of future rate adjustments was not source-reported. | source 1 |
| Oil supply and shipping routes | Shipping through the Strait of Hormuz was reported as effectively restricted due to the ongoing Iran conflict. | OPEC+ announced a production adjustment of 188k to 206k barrels per day. | The logistical capability to deliver adjusted supply volumes through the geographic chokepoint was not source-reported. | source 59 |
| Japan policy rate | The Bank of Japan held its short-term policy rate at 0.75%. | Three board members indicated preference for a rate increase. | The timing and magnitude of the next monetary policy rate adjustment were not source-reported. | source 41 |
| Utilities transaction | NextEra Energy and Dominion Energy announced a $67 billion all-stock combination. | The transaction requires approvals from three state and two federal regulatory commissions. | Regulatory approval outcomes and final closing status were not source-reported. | source 29 |
| Taiwan growth and geopolitical setting | Taiwan's economy expanded 13.7% in the first quarter. | The source report referenced cross-strait geopolitical tensions and evolving trade settings. | The net economic effect was not source-reported. | source 57 |

## 6. Scheduled Calendar

| date | event | publisher_or_entity | release_type_or_asset_group | consensus_or_forecast_if_source_reported | source |
| --- | --- | --- | --- | --- | --- |
| May 25, 2026 | Copom interest rate decision | Banco Central do Brasil | Brazil | not source-reported | source 47 |
| May 28, 2026 | Personal Income and Outlays (PCE) | Bureau of Economic Analysis | Monthly economic report | 3.2% (Core PCE) | source 108 |
| May 28, 2026 | Real Gross Domestic Product (GDP) | Bureau of Economic Analysis | Second estimate (Q1 2026) | not source-reported | source 22 |
| May 28, 2026 | SARB interest rate decision | South African Reserve Bank | South Africa | not source-reported | source 52 |
| May 30, 2026 | China Manufacturing PMI release | National Bureau of Statistics of China | China | not source-reported | source 78 |
| Jun 5, 2026 | Employment Situation | Bureau of Labor Statistics | Monthly economic report | 4.3% (Unemployment Rate) | source 109 |
| Jun 7, 2026 | OPEC+ monthly review meeting | OPEC | oil | not source-reported | source 59 |
| Jun 10, 2026 | Interest rate decision | European Central Bank | Monetary policy meeting / Europe | 85.0% probability of 2.25% | sources 110, 80 |
| Jun 10, 2026 | BoC interest rate decision | Bank of Canada | Canada | not source-reported | source 44 |
| Jun 10, 2026 | US Consumer Price Index release | Bureau of Labor Statistics | broad US equities | not source-reported | source 81 |
| Jun 15, 2026 | Industrial Production | Federal Reserve | Monthly economic report | 0.7% (MoM) | source 27 |
| Jun 15-16, 2026 | Monetary Policy Meeting | Bank of Japan | Monetary policy meeting / Japan | not source-reported | sources 111, 77 |
| Jun 16-17, 2026 | FOMC Meeting | Federal Reserve | Monetary policy meeting / cash and short-duration Treasuries | 95.9% probability of rate hold | sources 61, 5 |
| Jun 17, 2026 | Pending Home Sales | National Association of Realtors | Monthly economic report | not source-reported | source 57 |
| Jun 17, 2026 | Advance Monthly Retail Sales release | US Census Bureau | consumer discretionary | not source-reported | source 23 |
| Jun 18, 2026 | Interest Rate Decision | Bank of England | Monetary Policy Committee meeting / UK | not source-reported | sources 113, 40 |
| Jun 25, 2026 | Banxico interest rate decision | Bank of Mexico | Mexico | not source-reported | source 49 |

## 7. Missing Major Data

| data_area | missing_item | note |
| --- | --- | --- |
| Corporate Earnings | Broad-Index Earnings Aggregates (Q1 2026) | The provided macro report omitted comprehensive index-level earnings season financial metrics. |
| Central Bank Balance Sheet | Quantitative Easing/Tightening Totals | The provided macro report omitted the current nominal balance sheet size or specific run-off pace of the United States Federal Reserve System. |
| Consumer Credit | Outstanding Consumer Debt Metrics | The provided macro report did not include total revolving and non-revolving credit outstanding. |
| Housing Market | New Home Sales | The provided macro report did not include closed sales transaction volume for newly constructed single-family homes. |
| Trade Balance | International Trade in Goods and Services Deficit | The provided macro report did not include the exact nominal US trade-balance value for the March/April 2026 measurement periods. |
| Asset-Group Context | groups with no material recent fact found | The asset-group report listed value, size, dividend, low-volatility, momentum factors; communication services; consumer staples; healthcare; financials; industrials; materials; long Treasuries; TIPS; aggregate bonds; MBS; munis; investment-grade; high-yield; emerging-market bonds; developed ex-US; Australia; South Korea; agriculture; broad commodities; euro; yen; software; and AI infrastructure. |

## 8. Final Neutrality Statement

This briefing contains factual inputs only. It does not rank, recommend, analyze, or map facts to CapitalBench options.

## Options

Allowed option:
ID: CASH
Name: Cash / Do Not Invest
Symbol: N/A
Asset class: cash
Category: cash
Group: cash
Risk bucket: cash
Description: Cash position with no market exposure. Return is treated as 0 unless a round explicitly defines a cash yield proxy.

Allowed option:
ID: SHORT_TREASURY
Name: Short-Term Treasury Bills
Symbol: BIL
Asset class: cash_like
Category: treasury_bills
Group: cash_and_short_duration
Risk bucket: low
Description: Short-term US Treasury bill exposure. Typically used as a cash-like proxy with low duration risk.

Allowed option:
ID: SP500
Name: S&P 500
Symbol: SPY
Asset class: equity
Category: broad_us_equity
Group: us_broad_market
Risk bucket: medium
Description: Broad US large-cap equity exposure. Represents large publicly traded US companies across multiple sectors.

Allowed option:
ID: TOTAL_US_MARKET
Name: Total US Stock Market
Symbol: VTI
Asset class: equity
Category: broad_us_equity
Group: us_broad_market
Risk bucket: medium
Description: Broad exposure to the total US equity market, including large-, mid-, and small-cap companies. Useful as a diversified US equity proxy.

Allowed option:
ID: NASDAQ100
Name: Nasdaq 100
Symbol: QQQ
Asset class: equity
Category: growth_equity
Group: us_growth_and_technology
Risk bucket: high
Description: Large-cap, growth-oriented US equity exposure with heavy weights in technology and communication services. Sensitive to mega-cap earnings, rates, and growth-stock sentiment.

Allowed option:
ID: LARGE_GROWTH
Name: US Large-Cap Growth
Symbol: IWF
Asset class: equity
Category: style_factor
Group: us_style_factor
Risk bucket: high
Description: US large-cap growth stock exposure. Often tilted toward companies with higher expected growth, higher valuations, and greater sensitivity to interest rates.

Allowed option:
ID: LARGE_VALUE
Name: US Large-Cap Value
Symbol: IWD
Asset class: equity
Category: style_factor
Group: us_style_factor
Risk bucket: medium
Description: US large-cap value stock exposure. Often tilted toward companies with lower valuation multiples, dividends, financials, energy, and cyclical sectors.

Allowed option:
ID: MID_CAP
Name: US Mid-Cap Stocks
Symbol: IJH
Asset class: equity
Category: size_factor
Group: us_size_factor
Risk bucket: high
Description: US mid-cap equity exposure. Represents companies between large caps and small caps, with sensitivity to domestic growth, financing conditions, and risk appetite.

Allowed option:
ID: SMALL_CAP
Name: US Small-Cap Stocks
Symbol: IWM
Asset class: equity
Category: size_factor
Group: us_size_factor
Risk bucket: high
Description: US small-cap equity exposure. Often more sensitive to domestic economic growth, credit conditions, rates, and market risk appetite.

Allowed option:
ID: SMALL_VALUE
Name: US Small-Cap Value
Symbol: IWN
Asset class: equity
Category: style_and_size_factor
Group: us_style_factor
Risk bucket: high
Description: US small-cap value equity exposure. Combines smaller company exposure with value-oriented characteristics.

Allowed option:
ID: DIVIDEND
Name: US Dividend Equities
Symbol: SCHD
Asset class: equity
Category: dividend_equity
Group: us_factor_equity
Risk bucket: medium
Description: US dividend-oriented equity exposure. Often tilted toward profitable, mature companies with dividend histories.

Allowed option:
ID: LOW_VOL
Name: US Low Volatility Equities
Symbol: SPLV
Asset class: equity
Category: low_volatility_factor
Group: us_factor_equity
Risk bucket: medium
Description: US equity exposure focused on historically lower-volatility stocks. Often used as a defensive equity factor proxy.

Allowed option:
ID: MOMENTUM
Name: US Momentum Equities
Symbol: MTUM
Asset class: equity
Category: momentum_factor
Group: us_factor_equity
Risk bucket: high
Description: US equity exposure tilted toward stocks with stronger recent price momentum. Sensitive to trend persistence and factor rotations.

Allowed option:
ID: TECHNOLOGY
Name: Technology Sector
Symbol: XLK
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US technology sector exposure within large-cap equities. Includes software, hardware, semiconductors, and technology services companies.

Allowed option:
ID: COMMUNICATIONS
Name: Communication Services Sector
Symbol: XLC
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US communication services sector exposure. Includes large internet platforms, media, telecom, and entertainment companies.

Allowed option:
ID: CONSUMER_DISCRETIONARY
Name: Consumer Discretionary Sector
Symbol: XLY
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US consumer discretionary sector exposure. Sensitive to consumer spending, employment, credit conditions, and household confidence.

Allowed option:
ID: CONSUMER_STAPLES
Name: Consumer Staples Sector
Symbol: XLP
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US consumer staples sector exposure. Includes companies selling essential consumer products and is often considered a defensive equity sector.

Allowed option:
ID: HEALTHCARE
Name: Healthcare Sector
Symbol: XLV
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US healthcare sector exposure. Includes pharmaceuticals, biotechnology, medical devices, healthcare services, and insurers.

Allowed option:
ID: FINANCIALS
Name: Financials Sector
Symbol: XLF
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US financial sector exposure. Includes banks, insurers, capital markets firms, and financial services companies.

Allowed option:
ID: INDUSTRIALS
Name: Industrials Sector
Symbol: XLI
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US industrial sector exposure. Includes aerospace, machinery, transportation, logistics, and industrial services companies.

Allowed option:
ID: ENERGY
Name: Energy Sector
Symbol: XLE
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US energy sector exposure. Sensitive to oil and gas prices, production trends, geopolitics, and capital discipline.

Allowed option:
ID: MATERIALS
Name: Materials Sector
Symbol: XLB
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US materials sector exposure. Includes chemicals, metals, mining, packaging, and construction materials companies.

Allowed option:
ID: UTILITIES
Name: Utilities Sector
Symbol: XLU
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US utilities sector exposure. Often sensitive to interest rates, electricity demand, regulation, and defensive equity flows.

Allowed option:
ID: REAL_ESTATE
Name: Real Estate Sector
Symbol: XLRE
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US listed real estate equity exposure. Sensitive to interest rates, property fundamentals, credit conditions, and real estate valuations.

Allowed option:
ID: INTERMEDIATE_TREASURY
Name: Intermediate-Term US Treasury Bonds
Symbol: IEF
Asset class: bond
Category: treasury_duration
Group: bonds_and_rates
Risk bucket: medium
Description: Intermediate-duration US Treasury bond exposure. Sensitive to changes in interest rates, inflation expectations, and growth expectations.

Allowed option:
ID: LONG_TREASURY
Name: Long-Term US Treasury Bonds
Symbol: TLT
Asset class: bond
Category: treasury_duration
Group: bonds_and_rates
Risk bucket: high
Description: Long-duration US Treasury bond exposure. More sensitive to interest-rate changes than shorter-duration bond funds.

Allowed option:
ID: TIPS
Name: Treasury Inflation-Protected Securities
Symbol: TIP
Asset class: bond
Category: inflation_linked_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: US Treasury inflation-protected bond exposure. Sensitive to real interest rates and inflation expectations.

Allowed option:
ID: INVESTMENT_GRADE_CREDIT
Name: Investment Grade Corporate Bonds
Symbol: LQD
Asset class: bond
Category: corporate_credit
Group: credit
Risk bucket: medium
Description: US investment-grade corporate bond exposure. Sensitive to interest rates, credit spreads, and corporate balance-sheet conditions.

Allowed option:
ID: HIGH_YIELD_CREDIT
Name: High Yield Corporate Bonds
Symbol: HYG
Asset class: bond
Category: corporate_credit
Group: credit
Risk bucket: high
Description: US high-yield corporate bond exposure. Sensitive to credit spreads, default expectations, liquidity, and risk appetite.

Allowed option:
ID: AGGREGATE_BONDS
Name: US Aggregate Bond Market
Symbol: AGG
Asset class: bond
Category: aggregate_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: Broad US investment-grade bond market exposure. Includes Treasuries, agency securities, mortgage-backed securities, and corporate bonds.

Allowed option:
ID: DEVELOPED_EX_US
Name: Developed Markets ex-US
Symbol: VEA
Asset class: equity
Category: international_equity
Group: international_equity
Risk bucket: high
Description: Developed-market equity exposure outside the United States. Includes regions such as Europe, Japan, Canada, and developed Asia-Pacific markets.

Allowed option:
ID: EMERGING_MARKETS
Name: Emerging Markets
Symbol: VWO
Asset class: equity
Category: international_equity
Group: international_equity
Risk bucket: very_high
Description: Emerging-market equity exposure. Sensitive to global growth, currency moves, capital flows, commodity cycles, and country-specific policy risk.

Allowed option:
ID: EUROPE
Name: Europe Equities
Symbol: VGK
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: high
Description: European equity exposure. Sensitive to European growth, monetary policy, currency trends, energy costs, and regional earnings.

Allowed option:
ID: JAPAN
Name: Japan Equities
Symbol: EWJ
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: high
Description: Japanese equity exposure. Sensitive to Japanese corporate earnings, yen movements, monetary policy, and global trade conditions.

Allowed option:
ID: CHINA
Name: China Equities
Symbol: MCHI
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: very_high
Description: China equity exposure through publicly traded Chinese companies. Sensitive to Chinese growth, policy actions, currency moves, and geopolitical risk.

Allowed option:
ID: INDIA
Name: India Equities
Symbol: INDA
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: very_high
Description: Indian equity exposure. Sensitive to Indian economic growth, currency moves, domestic policy, valuations, and foreign capital flows.

Allowed option:
ID: GOLD
Name: Gold
Symbol: IAU
Asset class: commodity
Category: precious_metals
Group: commodities
Risk bucket: medium
Description: Gold exposure through a listed gold trust. Sensitive to real interest rates, US dollar strength, inflation expectations, and safe-haven demand.

Allowed option:
ID: BROAD_COMMODITIES
Name: Broad Commodities
Symbol: PDBC
Asset class: commodity
Category: broad_commodities
Group: commodities
Risk bucket: high
Description: Broad commodity exposure through a diversified commodity strategy ETF. Sensitive to energy, metals, agriculture, inflation expectations, and global demand.

Allowed option:
ID: SEMICONDUCTORS
Name: Semiconductors
Symbol: SMH
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: very_high
Description: Semiconductor equity exposure. Includes companies involved in chip design, manufacturing, equipment, and related supply chains.

Allowed option:
ID: SOFTWARE
Name: Software
Symbol: IGV
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: high
Description: Software equity exposure. Includes companies in application software, infrastructure software, and related technology services.

Allowed option:
ID: EQUAL_WEIGHT_SP500
Name: Equal-Weight S&P 500
Symbol: RSP
Asset class: equity
Category: broad_us_equity
Group: us_broad_market
Risk bucket: medium
Description: Equal-weight US large-cap equity exposure. Reduces concentration in the largest S&P 500 constituents compared with market-cap weighting.

Allowed option:
ID: BIOTECH
Name: Biotechnology
Symbol: XBI
Asset class: equity
Category: industry_equity
Group: healthcare_and_biotech
Risk bucket: very_high
Description: US biotechnology equity exposure. Sensitive to clinical data, financing conditions, regulation, mergers, and risk appetite.

Allowed option:
ID: REGIONAL_BANKS
Name: Regional Banks
Symbol: KRE
Asset class: equity
Category: industry_equity
Group: us_industry
Risk bucket: very_high
Description: US regional bank equity exposure. Sensitive to deposit trends, credit quality, yield curves, regulation, and commercial real estate conditions.

Allowed option:
ID: AEROSPACE_DEFENSE
Name: Aerospace and Defense
Symbol: ITA
Asset class: equity
Category: industry_equity
Group: us_industry
Risk bucket: high
Description: US aerospace and defense equity exposure. Sensitive to defense budgets, aircraft demand, supply chains, and geopolitical risk.

Allowed option:
ID: CANADA
Name: Canada Equities
Symbol: EWC
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: Canadian equity exposure through US-listed shares. Sensitive to financials, energy, materials, domestic growth, and Canadian dollar conditions.

Allowed option:
ID: UNITED_KINGDOM
Name: United Kingdom Equities
Symbol: EWU
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: United Kingdom equity exposure through US-listed shares. Sensitive to sterling, UK growth, global financials, energy, and dividend-oriented sectors.

Allowed option:
ID: AUSTRALIA
Name: Australia Equities
Symbol: EWA
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: Australian equity exposure through US-listed shares. Sensitive to banks, materials, commodity demand, China-linked growth, and Australian dollar conditions.

Allowed option:
ID: SOUTH_KOREA
Name: South Korea Equities
Symbol: EWY
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: South Korean equity exposure through US-listed shares. Sensitive to semiconductors, exports, won movements, global trade, and regional geopolitics.

Allowed option:
ID: TAIWAN
Name: Taiwan Equities
Symbol: EWT
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: Taiwan equity exposure through US-listed shares. Sensitive to semiconductor supply chains, global electronics demand, currency movements, and geopolitical risk.

Allowed option:
ID: BRAZIL
Name: Brazil Equities
Symbol: EWZ
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: Brazilian equity exposure through US-listed shares. Sensitive to commodities, rates, fiscal policy, currency moves, and emerging-market capital flows.

Allowed option:
ID: MEXICO
Name: Mexico Equities
Symbol: EWW
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: Mexican equity exposure through US-listed shares. Sensitive to domestic growth, currency moves, trade links, remittances, and nearshoring activity.

Allowed option:
ID: SOUTH_AFRICA
Name: South Africa Equities
Symbol: EZA
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: South African equity exposure through US-listed shares. Sensitive to resources, domestic policy, currency moves, power availability, and emerging-market flows.

Allowed option:
ID: MORTGAGE_BACKED_BONDS
Name: Agency Mortgage-Backed Bonds
Symbol: MBB
Asset class: bond
Category: securitized_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: US agency mortgage-backed securities exposure. Sensitive to interest rates, prepayment behavior, mortgage spreads, and housing finance conditions.

Allowed option:
ID: MUNICIPAL_BONDS
Name: Municipal Bonds
Symbol: MUB
Asset class: bond
Category: municipal_bonds
Group: bonds_and_rates
Risk bucket: low
Description: US municipal bond exposure. Sensitive to rates, state and local credit conditions, fund flows, and tax-exempt fixed-income demand.

Allowed option:
ID: EMERGING_MARKET_BONDS
Name: Emerging Market USD Bonds
Symbol: EMB
Asset class: bond
Category: emerging_market_debt
Group: credit
Risk bucket: high
Description: US dollar emerging-market bond exposure. Sensitive to sovereign spreads, US rates, currency stress, commodity cycles, and global risk appetite.

Allowed option:
ID: INTERNATIONAL_BONDS
Name: International Aggregate Bonds
Symbol: BNDX
Asset class: bond
Category: international_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: International investment-grade bond exposure. Sensitive to global rates, currency hedging, regional credit conditions, and non-US monetary policy.

Allowed option:
ID: SILVER
Name: Silver
Symbol: SLV
Asset class: commodity
Category: precious_metals
Group: commodities
Risk bucket: high
Description: Silver exposure through a listed trust. Sensitive to precious-metals demand, industrial usage, real rates, US dollar moves, and inflation expectations.

Allowed option:
ID: COPPER
Name: Copper
Symbol: CPER
Asset class: commodity
Category: industrial_metals
Group: commodities
Risk bucket: high
Description: Copper exposure through an exchange-traded product. Sensitive to industrial demand, China-linked growth, supply conditions, inventories, and electrification themes.

Allowed option:
ID: AGRICULTURE
Name: Agriculture Commodities
Symbol: DBA
Asset class: commodity
Category: agriculture
Group: commodities
Risk bucket: high
Description: Agricultural commodity exposure through a diversified exchange-traded product. Sensitive to weather, crop conditions, global demand, inventories, and currency moves.

Allowed option:
ID: OIL
Name: Crude Oil
Symbol: USO
Asset class: commodity
Category: energy_commodities
Group: commodities
Risk bucket: very_high
Description: Crude oil exposure through an exchange-traded product. Sensitive to supply, demand, inventories, OPEC policy, geopolitical risk, and futures-curve structure.

Allowed option:
ID: US_DOLLAR
Name: US Dollar
Symbol: UUP
Asset class: currency
Category: currency
Group: currencies
Risk bucket: medium
Description: US dollar currency exposure through an exchange-traded product. Sensitive to relative rates, global risk appetite, trade balances, and reserve-currency demand.

Allowed option:
ID: EURO
Name: Euro
Symbol: FXE
Asset class: currency
Category: currency
Group: currencies
Risk bucket: medium
Description: Euro currency exposure through an exchange-traded product. Sensitive to European rates, growth, fiscal policy, energy conditions, and US dollar movements.

Allowed option:
ID: YEN
Name: Japanese Yen
Symbol: FXY
Asset class: currency
Category: currency
Group: currencies
Risk bucket: high
Description: Japanese yen currency exposure through an exchange-traded product. Sensitive to Japanese monetary policy, rate differentials, carry trades, and safe-haven demand.

Allowed option:
ID: BITCOIN_ETF
Name: Bitcoin ETF
Symbol: IBIT
Asset class: crypto_proxy
Category: crypto_asset
Group: crypto_proxies
Risk bucket: very_high
Description: Bitcoin exposure through a US-listed spot bitcoin exchange-traded product. Sensitive to digital-asset flows, regulation, liquidity, rates, and risk appetite.

Allowed option:
ID: ETHEREUM_ETF
Name: Ethereum ETF
Symbol: ETHA
Asset class: crypto_proxy
Category: crypto_asset
Group: crypto_proxies
Risk bucket: very_high
Description: Ethereum exposure through a US-listed spot Ethereum exchange-traded product. Sensitive to digital-asset flows, network activity, regulation, liquidity, and risk appetite.
