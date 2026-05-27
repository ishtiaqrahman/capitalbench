# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make one-shot market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-week outcome window resolves.

This is a short-horizon weekly round. The scoring window is Tuesday-to-Tuesday:

- The entry price is the adjusted close from Tuesday, May 26, 2026.
- The decision deadline is Wednesday, May 27, 2026 at 04:00 America/Toronto / 08:00 UTC.
- The exit price is the adjusted close on Tuesday, June 2, 2026, calculated only after regular U.S. trading ends that Tuesday.
- The official score is based only on price movement from the May 26 adjusted close to the June 2 adjusted close.

Optimize only for the portfolio you expect to perform best over the May 26 close to June 2 close scoring window. Use longer-horizon facts only when they are likely to affect prices before the Tuesday, June 2 exit close.

Your objective is to allocate 100% across the allowed options to maximize expected one-week realized portfolio return, measured from the entry date to the exit date, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official one-shot leaderboard.

Your portfolio is scored by the weighted realized percentage return over the one-week round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

When reasoning, prioritize facts that can plausibly affect prices before the Tuesday, June 2 close: scheduled releases inside the window, known event dates, earnings or policy events inside the window, very near-term momentum, positioning, liquidity, and risks that could hit before the exit close. Use events after the June 2 close only if markets could price them before that close.

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

- Round ID: CB-2026-05-27-1W
- Decision date: 2026-05-27
- Research cutoff UTC: 2026-05-27T06:36:11Z
- Decision deadline UTC: 2026-05-27T08:00:00Z
- Horizon: one week
- Entry date: 2026-05-26
- Exit date: 2026-06-02
- Scoring window: 2026-05-26 to 2026-06-02; optimize for this one week window only.
- Close-to-close scoring: the entry price is the adjusted close on the entry date, and the exit price is the adjusted close on the exit date after regular trading ends.
- Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.
- Entry rule: Use adjusted close on Tuesday, May 26, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Tuesday, June 2, 2026 for each selected option; CASH return is 0 unless explicitly priced.
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
| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-05-27 | 0.00% | 0.00% | 0.00% | 0.00% | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-05-26 | 0.04% | 0.28% | 1.78% | 3.89% | pass |
| SP500 | SPY | us_broad_market | 2026-05-26 | 1.26% | 4.95% | 11.06% | 28.43% | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-05-26 | 1.45% | 4.80% | 11.14% | 28.51% | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-05-26 | 2.40% | 9.94% | 19.19% | 40.78% | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-05-26 | 0.80% | 4.73% | 6.11% | 26.11% | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-05-26 | 1.92% | 4.67% | 15.29% | 28.09% | pass |
| MID_CAP | IJH | us_size_factor | 2026-05-26 | 2.56% | 2.48% | 13.95% | 24.24% | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-05-26 | 3.80% | 4.82% | 18.08% | 41.37% | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-05-26 | 2.90% | 3.32% | 19.28% | 43.09% | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-05-26 | 1.71% | 4.95% | 21.23% | 29.16% | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-05-26 | 0.44% | 0.57% | 2.40% | 3.03% | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-05-26 | 4.83% | 11.86% | 27.25% | 37.29% | pass |
| TECHNOLOGY | XLK | us_sector | 2026-05-26 | 4.52% | 15.30% | 30.84% | 60.37% | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-05-26 | -0.47% | -0.22% | 1.60% | 14.88% | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-05-26 | 1.28% | 1.37% | 2.06% | 11.02% | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-05-26 | -2.21% | 1.57% | 7.43% | 4.38% | pass |
| HEALTHCARE | XLV | us_sector | 2026-05-26 | 0.94% | 3.52% | -5.47% | 14.37% | pass |
| FINANCIALS | XLF | us_sector | 2026-05-26 | 0.37% | 0.08% | -1.24% | 3.37% | pass |
| INDUSTRIALS | XLI | us_sector | 2026-05-26 | 2.09% | 1.04% | 14.77% | 23.25% | pass |
| ENERGY | XLE | us_sector | 2026-05-26 | -3.26% | 1.90% | 31.53% | 44.40% | pass |
| MATERIALS | XLB | us_sector | 2026-05-26 | 2.55% | -1.53% | 15.82% | 19.22% | pass |
| UTILITIES | XLU | us_sector | 2026-05-26 | 1.84% | -1.86% | 2.20% | 14.14% | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-05-26 | 0.63% | 2.81% | 9.71% | 11.96% | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-05-26 | 0.58% | -0.79% | -1.62% | 4.02% | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-05-26 | 1.42% | -1.00% | -3.99% | 3.78% | pass |
| TIPS | TIP | bonds_and_rates | 2026-05-26 | 0.41% | -0.35% | 0.48% | 4.70% | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-05-26 | 0.77% | -0.08% | -0.68% | 6.11% | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-05-26 | 0.40% | 0.11% | 1.99% | 7.00% | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-05-26 | 0.51% | -0.39% | -0.27% | 5.12% | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-05-26 | 2.25% | 5.45% | 19.31% | 32.72% | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-05-26 | 2.66% | 2.55% | 13.47% | 29.96% | pass |
| EUROPE | VGK | international_equity | 2026-05-26 | 1.41% | 3.39% | 12.05% | 19.83% | pass |
| JAPAN | EWJ | international_equity | 2026-05-26 | 1.85% | 5.95% | 15.80% | 29.68% | pass |
| CHINA | MCHI | international_equity | 2026-05-26 | -0.92% | -1.79% | -8.27% | 6.11% | pass |
| INDIA | INDA | international_equity | 2026-05-26 | 1.10% | -1.68% | -11.19% | -10.97% | pass |
| GOLD | IAU | commodities | 2026-05-26 | -0.84% | -3.70% | 8.12% | 36.11% | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-05-26 | -2.77% | -0.22% | 36.84% | 45.74% | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-05-26 | 6.64% | 18.94% | 73.70% | 146.56% | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-05-26 | 0.78% | 10.09% | -8.66% | -9.39% | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-05-26 | 1.87% | 2.90% | 9.89% | 18.88% | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-05-26 | 1.25% | 0.23% | 8.90% | 68.76% | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-05-26 | 1.63% | 0.33% | 12.62% | 24.82% | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-05-26 | 2.78% | 6.23% | 12.73% | 31.63% | pass |
| CANADA | EWC | country_equity | 2026-05-26 | 0.72% | 1.24% | 13.35% | 33.03% | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-05-26 | 0.76% | 1.74% | 12.45% | 23.11% | pass |
| AUSTRALIA | EWA | country_equity | 2026-05-26 | 0.17% | -0.82% | 14.05% | 15.56% | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-05-26 | 11.40% | 28.02% | 124.16% | 242.14% | pass |
| TAIWAN | EWT | country_equity | 2026-05-26 | 11.12% | 16.93% | 67.84% | 99.41% | pass |
| BRAZIL | EWZ | country_equity | 2026-05-26 | -0.71% | -8.52% | 12.94% | 37.51% | pass |
| MEXICO | EWW | country_equity | 2026-05-26 | 0.52% | 2.30% | 18.43% | 33.89% | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-05-26 | 1.88% | 0.06% | 8.58% | 43.55% | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-05-26 | 0.61% | -0.42% | 0.38% | 6.80% | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-05-26 | 0.68% | -0.44% | 0.90% | 5.81% | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-05-26 | 0.76% | 0.02% | 1.45% | 11.25% | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-05-26 | 0.65% | 0.61% | 0.16% | 2.27% | pass |
| SILVER | SLV | commodities | 2026-05-26 | 1.44% | 2.03% | 44.05% | 130.63% | pass |
| COPPER | CPER | commodities | 2026-05-26 | 1.19% | 5.69% | 22.58% | 31.64% | pass |
| AGRICULTURE | DBA | commodities | 2026-05-26 | -1.79% | -0.36% | 8.90% | 5.35% | pass |
| OIL | USO | commodities | 2026-05-26 | -5.04% | 1.69% | 95.60% | 103.63% | pass |
| US_DOLLAR | UUP | currencies | 2026-05-26 | 0.07% | 1.09% | 1.67% | 4.29% | pass |
| EURO | FXE | currencies | 2026-05-26 | 0.04% | -0.62% | 0.70% | 3.36% | pass |
| YEN | FXY | currencies | 2026-05-26 | -0.26% | 0.09% | -1.99% | -9.73% | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-05-26 | -2.27% | -1.31% | -15.76% | -31.22% | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-05-26 | -3.22% | -9.55% | -31.79% | -23.36% | pass |
## 3. Macro Snapshot
### Core Macro Table
| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inflation | CPI-U, all items | 0.6% | 0.9% in March 2026 | prior month | April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | CPI-U, all items | 3.8% | 3.3% for the 12 months ending March 2026 | prior 12-month rate | 12 months ending April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | CPI-U, all items less food and energy | 0.4% | 0.2% in March 2026 | prior month | April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | CPI-U, all items less food and energy | 2.8% | 2.6% for the 12 months ending March 2026 | prior 12-month rate | 12 months ending April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | PCE price index | 0.7% | 0.4% in February 2026 | prior month | March 2026 | April 30, 2026 | BEA Personal Income and Outlays |
| inflation | PCE price index | 3.5% | not source-reported | not source-reported | March 2026 from same month one year ago | April 30, 2026 | BEA Personal Income and Outlays |
| inflation | PCE price index excluding food and energy | 0.3% | 0.4% in February 2026 | prior month | March 2026 | April 30, 2026 | BEA Personal Income and Outlays |
| inflation | PCE price index excluding food and energy | 3.2% | not source-reported | not source-reported | March 2026 from same month one year ago | April 30, 2026 | BEA Personal Income and Outlays |
| inflation | Producer Price Index for final demand | 1.4% | not source-reported | not source-reported | April 2026 | May 2026 | BLS Producer Price Index |
| inflation | Producer Price Index for final demand | 6.0% | not source-reported | not source-reported | 12 months ending April 2026 | May 2026 | BLS Producer Price Index |
| labor | unemployment rate | 4.3% | unchanged at 4.3% | prior month | April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | nonfarm payroll employment | +115,000 jobs | not source-reported | not source-reported | April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | average hourly earnings for all employees on private nonfarm payrolls | +0.2% | same pace as the prior month | prior month | April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | average hourly earnings for all employees on private nonfarm payrolls | +3.6% | 3.4% in March 2026 | prior 12-month rate | 12 months ending April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | seasonally adjusted initial unemployment insurance claims | 209,000 | decrease of 3,000 from revised 212,000 | week-over-week change | week ending May 16, 2026 | May 21, 2026 | U.S. Department of Labor UI Claims |
| growth | real GDP | +2.0% annual rate | 0.5% in Q4 2025 | prior quarter | Q1 2026 advance estimate | April 30, 2026 | BEA GDP Advance Estimate |
| growth | retail and food services sales | $757.1 billion | up 0.5% from previous month and up 4.9% from April 2025 | month-over-month and year-over-year change | April 2026 | May 14, 2026 | U.S. Census Monthly Retail Trade |
| growth | current-dollar personal consumption expenditures | +0.9% | 0.6% in February 2026 | prior month | March 2026 | April 30, 2026 | BEA Personal Income and Outlays |
| growth | industrial production | +0.7% | -0.3% in March 2026 | prior month | April 2026 | May 15, 2026 | Federal Reserve G.17 |
| business surveys | ISM Manufacturing PMI | 52.7 | unchanged from March 2026 | prior month | April 2026 | May 1, 2026 | ISM Manufacturing PMI |
| business surveys | ISM Services PMI | 53.6 | 54.0 in March 2026 | prior month | April 2026 | May 5, 2026 | ISM Services PMI |
| consumer | University of Michigan Index of Consumer Sentiment | 44.8 | 49.8 in April 2026 and 52.2 in May 2025 | prior month and year-over-year comparison | May 2026 final | May 22, 2026 | University of Michigan Surveys of Consumers |
| consumer | Conference Board Consumer Confidence Index | 93.1 | down 0.7 points from upwardly revised 93.8 in April 2026 | prior month | May 2026 | May 26, 2026 | The Conference Board |
| housing | housing starts and building permits | starts 1,465,000 SAAR; permits 1,442,000 SAAR | starts down 2.8%; permits up 5.8% from March 2026 | month-over-month change | April 2026 | May 21, 2026 | Census/HUD New Residential Construction |
| housing | existing-home sales | 4.02 million SAAR | up 0.2% from March 2026 | month-over-month change | April 2026 | May 11, 2026 | AP / National Association of Realtors |
### Rates, Fed, Credit, Liquidity, Volatility
| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Federal Reserve policy | federal funds target range | 3.50% to 3.75% | not source-reported | not source-reported | current target range | April 30, 2026 | Federal Reserve Economy at a Glance |
| Federal Reserve policy | latest FOMC decision | maintain target range at 3.50% to 3.75% | not source-reported | not source-reported | April 2026 FOMC meeting | April 29, 2026 | Federal Reserve FOMC Statement |
| Federal Reserve policy | next scheduled FOMC meeting | June 16-17, 2026 | not source-reported | not source-reported | 2026 FOMC calendar | latest calendar page | Federal Reserve FOMC Calendar |
| Federal Reserve policy | CME FedWatch pricing cited by Kiplinger | 86% probability target range remains 3.50% to 3.75% through year-end | not source-reported | not source-reported | as cited after April 2026 FOMC decision | April 29, 2026 | Kiplinger / CME FedWatch |
| Treasury yields | 3-month Treasury par yield | 3.68% | not source-reported | not source-reported | May 26, 2026 | May 26, 2026 | U.S. Treasury Daily Treasury Rates |
| Treasury yields | 2-year Treasury par yield | 4.01% | not source-reported | not source-reported | May 26, 2026 | May 26, 2026 | U.S. Treasury Daily Treasury Rates |
| Treasury yields | 10-year Treasury par yield | 4.50% | not source-reported | not source-reported | May 26, 2026 | May 26, 2026 | U.S. Treasury Daily Treasury Rates |
| Treasury yields | 30-year Treasury par yield | 5.03% | not source-reported | not source-reported | May 26, 2026 | May 26, 2026 | U.S. Treasury Daily Treasury Rates |
| real rates | 10-year Treasury real yield | 2.10% | not source-reported | not source-reported | May 26, 2026 | May 26, 2026 | U.S. Treasury Daily Treasury Real Yield Curve Rates |
| inflation expectations | 10-year breakeven inflation rate | 2.40% | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | Equibles / FRED T10YIE |
| currency | U.S. Dollar Index futures | 99.037 | not source-reported | not source-reported | intraday quote | May 27, 2026 08:12 source time | Stooq DX.F Quote |
| volatility | CBOE Volatility Index | 16.70 | 16.76 prior value shown by source | prior observation | May 22, 2026 | May 22, 2026 | MacroMicro / CBOE VIX |
| volatility | ICE BofA MOVE Index | 78.43 | not source-reported | not source-reported | May 22, 2026 | May 22, 2026 | EODData MOVE Index |
| credit spreads | ICE BofA US Corporate Index option-adjusted spread | 0.75% | not source-reported | not source-reported | May 20, 2026 | May 20, 2026 | Equibles BAMLC0A0CM |
| credit spreads | ICE BofA US High Yield Index option-adjusted spread | 278 bps | 280 bps on May 20, 2026 | prior observation | May 21, 2026 | May 21, 2026 | Convex BAMLH0A0HYM2 |
| financial conditions | Chicago Fed National Financial Conditions Index | -0.523 | -0.516 prior week | prior week | week ending May 15, 2026 | May 2026 | YCharts / Chicago Fed NFCI |
| liquidity | total money market fund assets | $7.77 trillion | increased by $16.88 billion | week-over-week change | week ending May 20, 2026 | May 21, 2026 | Investment Company Institute |
| housing rates | 30-year fixed-rate mortgage average | 6.51% | 6.36% previous week | prior week | week ending May 21, 2026 | May 21, 2026 | Freddie Mac PMMS |
### Commodity And Currency State
| measure | latest_value | source_reported_comparison | comparison_type | observation_date | source |
| --- | --- | --- | --- | --- | --- |
| WTI crude futures | $91.74 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq CL.F Quote |
| Brent crude futures | $96.47 | up $3.05 from $93.42 | source-reported prior quote comparison | May 26, 2026 20:41 UTC | TECHi / Stooq Futures Snapshot |
| natural gas futures | 2.997 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq NG.F Quote |
| gold futures | 4527.05 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq GC.F Quote |
| silver futures | 7597.8 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq SI.F Quote |
| copper futures | 640.33 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq HG.F Quote |
| Bloomberg Commodity Total Return Index | 306.02 | up 2.52, or 0.83% | source-reported change | latest quote page crawl | Bloomberg Commodities |
| U.S. Dollar Index futures | 99.037 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq DX.F Quote |
| euro / U.S. dollar | 1.16402 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq EURUSD Quote |
| U.S. dollar / Japanese yen | 159.3615 | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq USDJPY Quote |
## 4. Asset-Group Context
| asset_group | covered_options_or_area | fact_type | factual_statement | source_reported_comparison | comparison_type | date_or_period | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cash and short-duration Treasuries | federal funds and Treasury bills | policy_or_regulatory_fact | The FOMC maintained the federal funds target range at 3.50% to 3.75%. | not source-reported | not source-reported | April 29, 2026 | Federal Reserve FOMC Statement |
| cash and short-duration Treasuries | money-market funds | observed_value | Total money market fund assets were $7.77 trillion. | increased by $16.88 billion | week-over-week change | week ending May 20, 2026 | Investment Company Institute |
| bonds and rates | Treasury curve | observed_value | The 3-month, 2-year, 10-year, and 30-year Treasury par yields were 3.68%, 4.01%, 4.50%, and 5.03%, respectively. | not source-reported | not source-reported | May 26, 2026 | U.S. Treasury Daily Treasury Rates |
| bonds and rates | TIPS | observed_value | The 10-year Treasury real yield was 2.10%. | not source-reported | not source-reported | May 26, 2026 | U.S. Treasury Daily Treasury Real Yield Curve Rates |
| bonds and rates | mortgages and MBS reference rates | observed_value | The 30-year fixed-rate mortgage average was 6.51%. | 6.36% previous week | prior value | week ending May 21, 2026 | Freddie Mac PMMS |
| credit | investment-grade credit | observed_value | The ICE BofA US Corporate Index option-adjusted spread was 0.75%. | not source-reported | not source-reported | May 20, 2026 | Equibles BAMLC0A0CM |
| credit | high-yield credit | observed_value | The ICE BofA US High Yield Index option-adjusted spread was 278 bps. | 280 bps on May 20, 2026 | prior value | May 21, 2026 | Convex BAMLH0A0HYM2 |
| broad US equities | S&P 500 earnings | observed_value | FactSet data cited by Axios reported S&P 500 Q1 2026 EPS of $80.75. | up 28.4% from Q1 2025 | year-over-year change | Q1 2026 | Axios / FactSet |
| broad US equities | valuation | observed_value | A May 2026 Shiller CAPE estimate for the S&P 500 was 41.6. | second-highest reading in more than 140 years of tracked data | range or percentile explicitly reported by source | May 2026 | Gotrade CAPE Ratio |
| Nasdaq / growth / technology | AI-linked earnings and cloud capex | labeled_forecast_or_estimate | Goldman Sachs Research said AI investment was expected to account for roughly 40% of S&P 500 earnings growth in 2026 and that the largest cloud computing companies planned estimated 2026 spending of $670 billion. | not source-reported | not source-reported | 2026 forecast, published April 2026 | Goldman Sachs Research |
| semiconductors | global chip sales | observed_value | Global semiconductor sales were $298.5 billion in Q1 2026. | up 25% from Q4 2025 | prior value | Q1 2026 | Semiconductor Industry Association |
| semiconductors | monthly global chip sales | observed_value | Global semiconductor sales were $99.5 billion in March 2026. | up 79.2% from March 2025 and up 11.5% from February 2026 | year-over-year and month-over-month change | March 2026 | Semiconductor Industry Association |
| AI/technology themes | AI infrastructure and electricity | labeled_forecast_or_estimate | IEA reported that capital expenditure of five large technology companies exceeded $400 billion in 2025 and was set to increase by a further 75% in 2026. | not source-reported | not source-reported | 2025 and 2026 forecast | IEA Energy and AI |
| AI/technology themes | quantum and advanced computing | policy_or_regulatory_fact | The U.S. Department of Commerce signed letters of intent for $2.013 billion in CHIPS Act incentives across nine quantum computing companies. | not source-reported | not source-reported | May 21, 2026 | NIST / Department of Commerce |
| consumer discretionary and consumer staples | retail sales categories | observed_value | U.S. retail and food services sales were $757.1 billion in April 2026. | up 0.5% from March 2026 and up 4.9% from April 2025 | month-over-month and year-over-year change | April 2026 | U.S. Census Monthly Retail Trade |
| real estate | residential property activity | observed_value | Existing-home sales were 4.02 million SAAR in April 2026. | up 0.2% from March 2026 | month-over-month change | April 2026 | AP / National Association of Realtors |
| real estate | housing construction | observed_value | Housing starts were 1,465,000 SAAR and building permits were 1,442,000 SAAR. | starts down 2.8%; permits up 5.8% from March 2026 | month-over-month change | April 2026 | Census/HUD New Residential Construction |
| aerospace/defense | defense budget request | policy_or_regulatory_fact | The FY2027 U.S. defense budget request was about $1.5 trillion, including a $1.15 trillion base request and $350 billion from reconciliation. | not source-reported | not source-reported | April 2026 | Breaking Defense |
| utilities | electricity demand and data centers | labeled_forecast_or_estimate | EIA forecast U.S. electricity load would increase by 1.9% in 2026 and 2.5% in 2027. | not source-reported | not source-reported | February 2026 STEO reference, published March 2026 | EIA Today in Energy |
| energy | oil supply policy | policy_or_regulatory_fact | Seven OPEC+ countries decided to implement a production adjustment of 188 thousand barrels per day from previous voluntary adjustments. | not source-reported | not source-reported | decision on May 3, 2026; adjustment for June 2026 | OPEC |
| energy | crude oil outlook | labeled_forecast_or_estimate | EIA expected global oil inventories to fall by an average of 8.5 million barrels per day in Q2 2026 and expected Brent prices around $106 per barrel in May and June. | not source-reported | not source-reported | May 2026 Short-Term Energy Outlook | EIA STEO |
| silver | precious metals | labeled_forecast_or_estimate | The Silver Institute projected the silver market would remain in deficit in 2026 for a sixth consecutive year, at 67 million ounces. | total global silver supply forecast to increase 1.5% to 1.05 billion ounces | consensus / forecast comparison | 2026 forecast, published February 2026 | The Silver Institute |
| copper and materials | base metals | labeled_forecast_or_estimate | S&P Global Market Intelligence said its 2026 average copper price forecast remained just above $12,100 per metric ton. | not source-reported | not source-reported | April 16, 2026 | S&P Global Market Intelligence |
| agriculture | grains | labeled_forecast_or_estimate | USDA forecast the U.S. corn crop at 16.0 billion bushels. | down 6% | year-over-year change | 2026/27 marketing year forecast, May 2026 WASDE | USDA WASDE |
| broad commodities | commodity index | observed_value | Bloomberg Commodity Total Return Index was quoted at 306.02. | up 2.52, or 0.83% | prior value | latest quote page crawl | Bloomberg Commodities |
| currencies | U.S. dollar, euro, yen | observed_value | U.S. Dollar Index futures, EUR/USD, and USD/JPY were quoted at 99.037, 1.16402, and 159.3615, respectively. | not source-reported | not source-reported | May 27, 2026 08:12 source time | Stooq FX Quotes |
| Europe equities | euro area growth and ECB policy | policy_or_regulatory_fact | The ECB held the deposit facility, main refinancing operations, and marginal lending facility rates at 2.00%, 2.15%, and 2.40%, respectively. | not source-reported | not source-reported | April 30, 2026 | European Central Bank |
| Europe equities | euro area GDP | observed_value | Euro area GDP increased by 0.1% quarter-over-quarter in Q1 2026. | not source-reported | not source-reported | Q1 2026 preliminary flash estimate | Eurostat |
| Japan equities | Japan policy rate and yen | policy_or_regulatory_fact | The Bank of Japan kept its benchmark rate unchanged at 0.75% in a 6-3 vote. | not source-reported | not source-reported | April 28, 2026 | AP / Bank of Japan |
| China equities | China credit policy and manufacturing | observed_value | China's one-year LPR was held at 3.0% and the five-year LPR was held at 3.5%. | not source-reported | not source-reported | May 2026 | Trading Economics China Interest Rate |
| China equities | manufacturing PMI | observed_value | China's official manufacturing PMI was 50.3 in April 2026. | down 0.1 percentage points from the previous month | month-over-month change | April 2026 | National Bureau of Statistics of China |
| India equities | India policy rates | policy_or_regulatory_fact | India's repo rate was listed at 5.25% and Standing Deposit Facility rate at 5.00%. | not source-reported | not source-reported | last updated May 2, 2026 | Bankopedia RBI Rates Dashboard |
| Canada equities | Canada policy rate | policy_or_regulatory_fact | The Bank of Canada held the overnight rate target at 2.25%, with the Bank Rate at 2.50% and deposit rate at 2.20%. | not source-reported | not source-reported | April 29, 2026 | Bank of Canada |
| UK equities | UK policy rate | policy_or_regulatory_fact | The Bank of England MPC voted 8-1 to maintain Bank Rate at 3.75%. | not source-reported | not source-reported | April 30, 2026 | Bank of England |
| crypto proxies | bitcoin and ethereum ETFs | observed_value | CryptoETF.today listed 24-hour net flows of -$105.2 million for bitcoin ETFs and -$6.6 million for ethereum ETFs. | YTD net inflows listed as +$535.5 million for bitcoin ETFs and -$701.9 million for ethereum ETFs | year-to-date change | May 27, 2026 live page | CryptoETF.today |
## 5. Tension Ledger
| area_or_asset_group | source_reported_fact_1 | source_reported_fact_2 | unresolved_question | source_or_sources |
| --- | --- | --- | --- | --- |
| inflation and labor | CPI-U rose 3.8% over the 12 months ending April 2026 | nonfarm payroll employment increased by 115,000 in April 2026 | May 2026 CPI and Employment Situation releases | BLS CPI; BLS Employment Situation |
| consumer and spending | University of Michigan consumer sentiment was 44.8 in May 2026 | current-dollar PCE increased 0.9% in March 2026 | April 2026 PCE price index and personal spending release | University of Michigan; BEA Personal Income and Outlays |
| rates and credit | 10-year Treasury par yield was 4.50% on May 26, 2026 | ICE BofA US High Yield Index OAS was 278 bps on May 21, 2026 | June 16-17, 2026 FOMC policy decision | U.S. Treasury; Convex BAMLH0A0HYM2 |
| housing | 30-year fixed-rate mortgage average was 6.51% for the week ending May 21, 2026 | existing-home sales were 4.02 million SAAR in April 2026 | May 2026 existing-home sales release | Freddie Mac; AP / NAR |
| energy and inflation | WTI crude futures were $91.74 on May 27, 2026 source time | CPI energy index increased 17.9% over the 12 months ending April 2026 | May 2026 CPI energy index release | Stooq CL.F; BLS CPI |
| policy calendar | federal funds target range was 3.50% to 3.75% | ECB deposit facility rate was 2.00%, main refinancing operations rate was 2.15%, and marginal lending facility rate was 2.40% | June 2026 FOMC and ECB policy decisions | Federal Reserve; ECB |
| broad US equities | S&P 500 Q1 2026 EPS was $80.75, up 28.4% from Q1 2025. | The May 2026 Shiller CAPE estimate for the S&P 500 was 41.6. | Next FactSet Earnings Insight update | Axios / FactSet; Gotrade CAPE Ratio |
| semiconductors | Global semiconductor sales were $298.5 billion in Q1 2026, up 25% from Q4 2025. | The U.S. Commerce Department signed letters of intent for $2.013 billion in quantum-computing CHIPS Act incentives. | Next monthly SIA semiconductor sales release | SIA; NIST |
| AI infrastructure and utilities | IEA reported data-centre electricity demand rose 17% in 2025. | EIA forecast U.S. electricity load would increase by 1.9% in 2026 and 2.5% in 2027. | Next EIA electricity-demand forecast update | IEA; EIA |
| energy/oil | Seven OPEC+ countries decided on a 188 thousand barrels per day production adjustment for June 2026. | EIA expected global oil inventories to fall by an average of 8.5 million barrels per day in Q2 2026. | June 7, 2026 OPEC+ review meeting and June 9, 2026 EIA STEO release | OPEC; EIA STEO |
| international equities | The ECB held its three key rates at 2.00%, 2.15%, and 2.40%. | Euro area GDP increased by 0.1% quarter-over-quarter in Q1 2026. | June 11, 2026 ECB monetary policy decision | ECB; Eurostat |
| crypto proxies | Bitcoin ETFs had 24-hour net flows of -$105.2 million. | Bitcoin ETF YTD net inflows were listed as +$535.5 million. | Next settled U.S. spot crypto ETF flow update | CryptoETF.today |
## 6. Scheduled Calendar
| date | event | publisher_or_entity | release_type_or_asset_group | consensus_or_forecast_if_source_reported | source |
| --- | --- | --- | --- | --- | --- |
| May 28, 2026 8:30 AM ET | GDP second estimate and corporate profits, Q1 2026 | U.S. Bureau of Economic Analysis | economic data release | not source-reported | BEA Release Schedule |
| May 28, 2026 8:30 AM ET | Personal Income and Outlays, April 2026 | U.S. Bureau of Economic Analysis | economic data release | not source-reported | BEA Release Schedule |
| June 1, 2026 10:00 AM ET | ISM Manufacturing PMI, May 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar |
| June 3, 2026 10:00 AM ET | ISM Services PMI, May 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar |
| June 5, 2026 8:30 AM ET | Employment Situation, May 2026 | U.S. Bureau of Labor Statistics | labor market release | not source-reported | BLS 2026 Release Calendar |
| June 10, 2026 8:30 AM ET | CPI, May 2026 | U.S. Bureau of Labor Statistics | inflation release | not source-reported | BLS CPI Release Schedule |
| June 11, 2026 8:30 AM ET | Producer Price Index, May 2026 | U.S. Bureau of Labor Statistics | inflation release | not source-reported | BLS PPI |
| June 11, 2026 | Governing Council monetary policy meeting, day 2, followed by press conference | European Central Bank | monetary policy decision | not source-reported | ECB Governing Council Calendar |
| June 16-17, 2026 | FOMC meeting | Federal Reserve | monetary policy decision | not source-reported | Federal Reserve FOMC Calendar |
| June 16-17, 2026 | Monetary Policy Meeting | Bank of Japan | monetary policy decision | not source-reported | Bank of Japan MPM Schedule |
| June 18, 2026 | Monetary Policy Committee decision | Bank of England | monetary policy decision | not source-reported | Bank of England Bank Rate Page |
| June 22, 2026 01:15 AM | China Loan Prime Rate 1Y and 5Y | People's Bank of China / National Interbank Funding Center | monetary policy rate fixing | prior 1Y LPR 3.0%; prior 5Y LPR 3.5% | Trading Economics China LPR Calendar |
| May 29, 2026 | FactSet Earnings Insight update | FactSet | broad US equities | not source-reported | International Daily Finance citing FactSet schedule |
| May 30, 2026 9:30 PM ET | China NBS PMI release | National Bureau of Statistics of China | China equities | not source-reported | MTS Insights China NBS PMIs |
| June 7, 2026 | OPEC+ monthly review meeting referenced after May 3 decision | OPEC+ | energy/oil | not source-reported | AP / OPEC+ |
| June 9, 2026 | Short-Term Energy Outlook next release | U.S. Energy Information Administration | energy/oil | not source-reported | EIA STEO |
## 7. Missing Major Data
| data_area | missing_item | note |
| --- | --- | --- |
| inflation | April 2026 PCE price index and core PCE price index | scheduled for May 28, 2026 |
| growth | Q1 2026 GDP second estimate and corporate profits | scheduled for May 28, 2026 |
| labor | May 2026 Employment Situation | scheduled for June 5, 2026 |
| inflation | May 2026 CPI | scheduled for June 10, 2026 |
| inflation | May 2026 PPI | scheduled for June 11, 2026 |
| business surveys | May 2026 ISM Manufacturing PMI and ISM Services PMI | scheduled for June 1 and June 3, 2026 |
| growth | May 2026 retail sales | not released in source set |
| housing | May 2026 housing starts, building permits, and existing-home sales | not released in source set |
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

