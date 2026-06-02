# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make one-shot market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

Research cutoff: 2026-06-02T03:44:23Z.
Decision deadline: 2026-06-02T08:00:00Z.
Entry price: adjusted close on Monday, June 1, 2026, the latest available official close before the decision deadline.
Exit price: adjusted close on Wednesday, July 1, 2026.

The scoring timeline is central to the task: this is a one-month round measured from the June 1, 2026 adjusted close to the July 1, 2026 adjusted close. The result is calculated after regular U.S. trading ends on Wednesday, July 1, 2026. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that July 1 exit close.

Optimize only for the portfolio you expect to perform best over the June 1 close to July 1 close one-month scoring window. Use longer-horizon facts only when they are likely to affect prices before the July 1 exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical return table. Treat inclusion, section order, grouping, row count, and trailing-return table order as context, not recommendation signals.

Your objective is to allocate 100% across the allowed options to maximize expected one-month realized portfolio return, measured from the June 1, 2026 adjusted close to the July 1, 2026 adjusted close, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official one-shot leaderboard.

Your portfolio is scored by the weighted realized percentage return over the June 1 close to July 1 close one-month round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

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

- Round ID: CB-2026-06-02-1M
- Decision date: 2026-06-02
- Research cutoff UTC: 2026-06-02T03:44:23Z
- Decision deadline UTC: 2026-06-02T08:00:00Z
- Horizon: one month
- Entry date: 2026-06-01
- Exit date: 2026-07-01
- Scoring window: 2026-06-01 to 2026-07-01; optimize for this one month window only.
- Close-to-close scoring: the entry price is the adjusted close on the entry date, and the exit price is the adjusted close on the exit date after regular trading ends.
- Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.
- Input-bias control: treat fact inclusion, section order, grouping, and trailing-return table order as context, not recommendations; do not infer expected return from mention count or placement.
- Entry rule: Use adjusted close on Monday, June 1, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Wednesday, July 1, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Submission format: portfolio
- Scoring benchmark: S&P 500 / SPY
- Return calculation: adjusted close prices are used when available.
- Portfolio holdings allowed: 1-5
- Portfolio allocation increment: 5%
- Portfolio minimum allocation: 5%
- Portfolio total allocation: 100%

## Briefing

# CapitalBench Briefing

## 1. Neutrality And Bias-Control Statement

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Missing rows are preserved for comparability; inclusion, order, grouping, and row count are not evidence of expected return.

## 2. Research And Evaluation Setup

| field | value |
|---|---|
| research cutoff | 2026-06-02T03:44:23Z |
| decision deadline | 2026-06-02T08:00:00Z |
| evaluation horizon | one month |
| entry date | 2026-06-01 |
| exit date | 2026-07-01 |
| model access rule | no tool use and no web access |
| shared-input rule | competing models receive the same frozen factual briefing, fixed ETF option universe, and mechanical return table |

## 3. Core Macro Datapoints

| indicator_id | data_area | measure | latest_value | unit | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source | status |
|---|---|---|---:|---|---|---|---|---|---|---|
| CPI_HEADLINE_MOM | inflation | CPI-U, all items | 0.6 | % MoM | 0.9% in March 2026 | prior value | April 2026 | May 12, 2026 | BLS CPI News Release | observed |
| CPI_HEADLINE_YOY | inflation | CPI-U, all items | 3.8 | % YoY | 3.3% for the 12 months ending March 2026 | prior value | 12 months ending April 2026 | May 12, 2026 | BLS CPI News Release | observed |
| CPI_CORE_MOM | inflation | CPI-U, all items less food and energy | 0.4 | % MoM | 0.2% in March 2026 | prior value | April 2026 | May 12, 2026 | BLS CPI News Release | observed |
| CPI_CORE_YOY | inflation | CPI-U, all items less food and energy | 2.8 | % YoY | 2.6% for the 12 months ending March 2026 | prior value | 12 months ending April 2026 | May 12, 2026 | BLS CPI News Release | observed |
| CPI_SHELTER_MOM | inflation | CPI-U shelter index | 0.6 | % MoM | 0.3% in March 2026 | prior value | April 2026 | May 12, 2026 | BLS CPI News Release | observed |
| CPI_ENERGY_MOM | inflation | CPI-U energy index | 3.8 | % MoM | 10.9% in March 2026 | prior value | April 2026 | May 12, 2026 | BLS CPI News Release | observed |
| PCE_HEADLINE_MOM | inflation | PCE price index | 0.4 | % MoM | 0.7% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| PCE_HEADLINE_YOY | inflation | PCE price index | 3.8 | % YoY | not source-reported | not source-reported | April 2026 from same month one year ago | May 28, 2026 | BEA Personal Income and Outlays | observed |
| PCE_CORE_MOM | inflation | PCE price index excluding food and energy | 0.2 | % MoM | 0.3% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| PCE_CORE_YOY | inflation | PCE price index excluding food and energy | 3.3 | % YoY | not source-reported | not source-reported | April 2026 from same month one year ago | May 28, 2026 | BEA Personal Income and Outlays | observed |
| PCE_GOODS_MOM | inflation | PCE goods price index | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| PCE_SERVICES_MOM | inflation | PCE services price index | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| PPI_FINAL_DEMAND_MOM | inflation | Producer Price Index for final demand | 1.4 | % MoM | 0.7% in March 2026 and 0.6% in February 2026 | prior value | April 2026 | May 13, 2026 | BLS Producer Price Index | observed |
| PPI_FINAL_DEMAND_YOY | inflation | Producer Price Index for final demand | 6.0 | % YoY | 4.3% in March 2026 | prior value | 12 months ending April 2026 | May 13, 2026 | BLS Producer Price Index | observed |
| UNEMPLOYMENT_RATE | labor | U-3 unemployment rate | 4.3 | % | unchanged at 4.3% | prior value | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| U6_UNEMPLOYMENT_RATE | labor | U-6 unemployment rate | 8.2 | % | 8.0% in March 2026 | prior value | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| LABOR_FORCE_PARTICIPATION_RATE | labor | labor force participation rate | 61.8 | % | 61.9% in March 2026 | prior value | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| NONFARM_PAYROLLS | labor | nonfarm payroll employment change | 115000 | jobs | March 2026 revised to +185,000 jobs | prior value | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| AVERAGE_HOURLY_EARNINGS_MOM | labor | average hourly earnings for all employees on private nonfarm payrolls | 0.2 | % MoM | not source-reported | not source-reported | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| AVERAGE_HOURLY_EARNINGS_YOY | labor | average hourly earnings for all employees on private nonfarm payrolls | 3.6 | % YoY | not source-reported | not source-reported | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| AVERAGE_WEEKLY_HOURS | labor | average weekly hours of all employees on private nonfarm payrolls | 34.3 | hours | 34.2 in March 2026 | prior value | April 2026 | May 8, 2026 | BLS Employment Situation | observed |
| INITIAL_JOBLESS_CLAIMS | labor | seasonally adjusted initial unemployment insurance claims | 215000 | claims | increase of 5,000 from previous week's revised level | week-over-week change | week ending May 23, 2026 | May 28, 2026 | U.S. Department of Labor UI Claims | observed |
| CONTINUING_JOBLESS_CLAIMS | labor | insured unemployment, continued claims | 1786000 | claims | not source-reported | not source-reported | week ending May 16, 2026 | May 29, 2026 | FRED CCSA | observed |
| JOLTS_JOB_OPENINGS | labor | job openings, total nonfarm | 6866 | thousands | 6,922 thousand in February 2026 | prior value | March 2026 | May 6, 2026 | FRED JTSJOL | observed |
| REAL_GDP_QOQ_SAAR | growth | real GDP | 1.6 | % QoQ SAAR | revised down 0.4 percentage point from the advance estimate; Q4 2025 was +0.5% | revision and prior value | Q1 2026 second estimate | May 28, 2026 | BEA GDP Second Estimate | observed |
| GDP_PRICE_INDEX | growth | gross domestic product price index | 3.8 | % QoQ SAAR | revised up 0.1 percentage point from the advance estimate | revision | Q1 2026 second estimate | May 28, 2026 | BEA GDP Second Estimate | observed |
| RETAIL_SALES_MOM | growth | advance retail and food services sales | 0.5 | % MoM | up 4.9% from April 2025 | year-over-year change | April 2026 | May 14, 2026 | U.S. Census Monthly Retail Trade | observed |
| RETAIL_SALES_YOY | growth | advance retail and food services sales | 4.9 | % YoY | up 0.5% from previous month | month-over-month change | April 2026 | May 14, 2026 | U.S. Census Monthly Retail Trade | observed |
| RETAIL_SALES_CONTROL_GROUP_MOM | growth | retail sales control group | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| PERSONAL_INCOME_MOM | growth | personal income | -0.1 | % MoM | 0.5% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| PERSONAL_SPENDING_MOM | growth | current-dollar personal consumption expenditures | 0.5 | % MoM | 1.0% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| PERSONAL_SAVING_RATE | growth | personal saving as a percentage of disposable personal income | 2.6 | % | not source-reported | not source-reported | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| CONSUMER_CREDIT | consumer credit | total consumer credit owned and securitized | 5140540.72 | USD millions | not source-reported | not source-reported | March 2026 | May 2026 | FRED TOTALSL | observed |
| DURABLE_GOODS_ORDERS_MOM | manufacturing | new orders for manufactured durable goods | 7.9 | % MoM | 1.3% in March 2026 | prior value | April 2026 advance | May 27, 2026 | Census Advance Report on Durable Goods | observed |
| FACTORY_ORDERS_MOM | manufacturing | manufacturers' new orders | 1.5 | % MoM | not source-reported | not source-reported | March 2026 | May 5, 2026 | Census Manufacturers' Shipments, Inventories, and Orders | observed |
| US_TRADE_BALANCE | trade | international trade in goods and services balance | -60307 | USD millions | -57,777 million in February 2026 | prior value | March 2026 | May 2026 | FRED BOPGSTB | observed |
| INDUSTRIAL_PRODUCTION_MOM | production | industrial production index | 0.7 | % MoM | -0.3% in March 2026; 1.4% above April 2025 | prior value and year-over-year change | April 2026 | May 15, 2026 | Federal Reserve G.17 | observed |
| CAPACITY_UTILIZATION | production | capacity utilization, total industry | 76.1194 | % | not source-reported | not source-reported | April 2026 | May 15, 2026 | FRED TCU | observed |
| ISM_MANUFACTURING_PMI | business surveys | ISM Manufacturing PMI | 54.0 | index | 52.7 in April 2026; up 1.3 percentage points | prior value and month-over-month change | May 2026 | June 1, 2026 | ISM Manufacturing PMI | observed |
| ISM_MANUFACTURING_NEW_ORDERS | business surveys | ISM Manufacturing New Orders Index | 56.8 | index | 54.1 in April 2026; up 2.7 percentage points | prior value and month-over-month change | May 2026 | June 1, 2026 | ISM Manufacturing PMI | observed |
| ISM_MANUFACTURING_PRICES | business surveys | ISM Manufacturing Prices Index | 82.1 | index | 84.6 in April 2026; down 2.5 percentage points | prior value and month-over-month change | May 2026 | June 1, 2026 | ISM Manufacturing PMI | observed |
| ISM_MANUFACTURING_EMPLOYMENT | business surveys | ISM Manufacturing Employment Index | 48.6 | index | 46.4 in April 2026; up 2.2 percentage points | prior value and month-over-month change | May 2026 | June 1, 2026 | ISM Manufacturing PMI | observed |
| ISM_SERVICES_PMI | business surveys | ISM Services PMI | 53.6 | index | 54.0 in March 2026 | prior value | April 2026 | May 5, 2026 | ISM Services PMI | observed |
| ISM_SERVICES_NEW_ORDERS | business surveys | ISM Services New Orders Index | 52.9 | index | 54.2 in March 2026 | prior value | April 2026 | May 5, 2026 | ISM Services PMI | observed |
| ISM_SERVICES_PRICES | business surveys | ISM Services Prices Index | 65.1 | index | 64.3 in March 2026 | prior value | April 2026 | May 5, 2026 | ISM Services PMI | observed |
| ISM_SERVICES_EMPLOYMENT | business surveys | ISM Services Employment Index | 51.7 | index | 51.5 in March 2026 | prior value | April 2026 | May 5, 2026 | ISM Services PMI | observed |
| CONSUMER_SENTIMENT | consumer | University of Michigan Index of Consumer Sentiment | 44.8 | index | 49.8 in April 2026 and 52.2 in May 2025 | prior value and year-over-year change | May 2026 final | May 22, 2026 | University of Michigan Surveys of Consumers | observed |
| CONSUMER_INFLATION_EXPECTATIONS_1Y | consumer | University of Michigan expected change in prices during next year | 4.7 | % | 3.8% in March 2026 | prior value | April 2026 | May 2026 | FRED MICH | observed |
| CONSUMER_INFLATION_EXPECTATIONS_5Y | consumer | University of Michigan expected change in prices during next 5 to 10 years | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| CONSUMER_CONFIDENCE | consumer | Conference Board Consumer Confidence Index | 93.1 | index | down 0.7 points from upwardly revised 93.8 in April 2026 | prior value | May 2026 | May 26, 2026 | The Conference Board Consumer Confidence | observed |
| HOUSING_STARTS | housing | housing starts | 1465000 | SAAR | down 2.8% from revised March 2026 and up 4.6% from April 2025 | month-over-month and year-over-year change | April 2026 | May 21, 2026 | Census/HUD New Residential Construction | observed |
| BUILDING_PERMITS | housing | building permits | 1423000 | SAAR | not source-reported | not source-reported | April 2026 | May 2026 | FRED PERMIT | observed |
| EXISTING_HOME_SALES | housing | existing-home sales | 4020000 | SAAR | increased by 0.2% in April 2026 | month-over-month change | April 2026 | May 2026 | National Association of Realtors Existing-Home Sales | observed |
| NEW_HOME_SALES | housing | new one-family houses sold | 622000 | SAAR | not source-reported | not source-reported | April 2026 | May 2026 | FRED HSN1F | observed |
| PENDING_HOME_SALES | housing | pending home sales index | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |

## 4. Rates Credit Liquidity Volatility Datapoints

| indicator_id | data_area | measure | latest_value | unit | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source | status |
|---|---|---|---:|---|---|---|---|---|---|---|
| FED_FUNDS_TARGET_RANGE | Federal Reserve policy | federal funds target range | 3.50 to 3.75 | % | not source-reported | not source-reported | current target range | April 29, 2026 | Federal Reserve FOMC Statement | observed |
| LATEST_FOMC_DECISION | Federal Reserve policy | latest FOMC decision | maintain target range at 3.50% to 3.75% | text | not source-reported | not source-reported | April 2026 FOMC meeting | April 29, 2026 | Federal Reserve FOMC Statement | observed |
| NEXT_FOMC_MEETING | Federal Reserve policy | next scheduled FOMC meeting | June 16-17, 2026 | date range | not source-reported | not source-reported | 2026 FOMC calendar | May 20, 2026 calendar update | Federal Reserve FOMC Calendar | scheduled |
| MARKET_IMPLIED_NEXT_FOMC_PROBABILITY | Federal Reserve policy | June 17, 2026 target-rate probability for 3.50% to 3.75% | 99.4 | % | 99.1% previous day and 96.5% previous week | prior value and week-over-week change | updated May 29, 2026 5:25 PM EDT | May 29, 2026 | Investing.com Fed Rate Monitor Tool | observed |
| EFFECTIVE_FED_FUNDS_RATE | Federal Reserve policy | effective federal funds rate | 3.62 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DFF | observed |
| SOFR | Federal Reserve policy | Secured Overnight Financing Rate | 3.63 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED SOFR | observed |
| TREASURY_3M | Treasury yields | 3-month Treasury constant maturity rate | 3.69 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS3MO | observed |
| TREASURY_2Y | Treasury yields | 2-year Treasury constant maturity rate | 3.98 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS2 | observed |
| TREASURY_5Y | Treasury yields | 5-year Treasury constant maturity rate | 4.13 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS5 | observed |
| TREASURY_10Y | Treasury yields | 10-year Treasury constant maturity rate | 4.45 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS10 | observed |
| TREASURY_30Y | Treasury yields | 30-year Treasury constant maturity rate | 4.99 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS30 | observed |
| REAL_YIELD_5Y | real rates | 5-year Treasury inflation-indexed security constant maturity rate | 1.61 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DFII5 | observed |
| REAL_YIELD_10Y | real rates | 10-year Treasury inflation-indexed security constant maturity rate | 2.07 | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DFII10 | observed |
| BREAKEVEN_INFLATION_5Y | inflation expectations | 5-year breakeven inflation rate | 2.54 | % | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 | FRED T5YIE | observed |
| BREAKEVEN_INFLATION_10Y | inflation expectations | 10-year breakeven inflation rate | 2.40 | % | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 | FRED T10YIE | observed |
| INFLATION_SWAP_OR_MARKET_EXPECTATION_1Y | inflation expectations | 1-year market inflation expectation | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| TREASURY_10Y_2Y_SPREAD | Treasury spreads | 10-year Treasury minus 2-year Treasury constant maturity spread | 0.42 | percentage points | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 | FRED T10Y2Y | observed |
| TREASURY_10Y_3M_SPREAD | Treasury spreads | 10-year Treasury minus 3-month Treasury constant maturity spread | 0.69 | percentage points | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 | FRED T10Y3M | observed |
| US_DOLLAR_INDEX | currency | U.S. Dollar Index futures | 99.142 | index | not source-reported | not source-reported | June 1, 2026 source timestamp | June 1, 2026 22:58:08 source time | Stooq DX.F Quote | observed |
| VIX | volatility | CBOE Volatility Index | 15.32 | index | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED VIXCLS | observed |
| MOVE_INDEX | volatility | ICE BofA MOVE Index | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| INVESTMENT_GRADE_OAS | credit spreads | ICE BofA US Corporate Index option-adjusted spread | 0.74 | % | not source-reported | not source-reported | May 31, 2026 | May 31, 2026 | FRED BAMLC0A0CM | observed |
| HIGH_YIELD_OAS | credit spreads | ICE BofA US High Yield Index option-adjusted spread | 2.74 | % | not source-reported | not source-reported | May 31, 2026 | May 31, 2026 | FRED BAMLH0A0HYM2 | observed |
| FINANCIAL_CONDITIONS_INDEX | financial conditions | Chicago Fed National Financial Conditions Index | -0.510 | index | not source-reported | not source-reported | week ending May 22, 2026 | May 22, 2026 | FRED NFCI | observed |
| MONEY_MARKET_FUND_ASSETS | liquidity | total money market fund assets | 7.78 | USD trillions | increased by $13.39 billion | week-over-week change | week ending May 27, 2026 | May 28, 2026 | Investment Company Institute Money Market Fund Assets | observed |
| FED_BALANCE_SHEET_TOTAL_ASSETS | liquidity | Federal Reserve total assets | 6704383 | USD millions | not source-reported | not source-reported | week ending May 27, 2026 | May 27, 2026 | FRED WALCL | observed |
| RESERVE_BALANCES_WITH_FEDERAL_RESERVE | liquidity | reserve balances with Federal Reserve Banks | 3066560 | USD millions | not source-reported | not source-reported | week ending May 27, 2026 | May 27, 2026 | FRED WRESBAL | observed |
| TREASURY_GENERAL_ACCOUNT | liquidity | Treasury General Account balance | 830296 | USD millions | not source-reported | not source-reported | week ending May 27, 2026 | May 27, 2026 | FRED WTREGEN | observed |
| REVERSE_REPO | liquidity | overnight reverse repurchase agreements | 1.302 | USD billions | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 | FRED RRPONTSYD | observed |
| M2_MONEY_STOCK | liquidity | M2 money stock | 22804.5 | USD billions | not source-reported | not source-reported | April 2026 | May 2026 | FRED M2SL | observed |
| MORTGAGE_30Y_FIXED_RATE | housing rates | 30-year fixed-rate mortgage average | 6.53 | % | 6.51% previous week | prior value | week ending May 28, 2026 | May 28, 2026 | FRED MORTGAGE30US | observed |

## 5. Commodity And Currency Datapoints

| indicator_id | measure | latest_value | unit | source_reported_comparison | comparison_type | observation_date | source | status |
|---|---|---:|---|---|---|---|---|---|
| WTI_CRUDE | WTI crude futures | 92.31 | USD per barrel | not source-reported | not source-reported | June 2, 2026 01:11:14 source time | Stooq CL.F Quote | observed |
| BRENT_CRUDE | Brent crude spot | 102.75 | USD per barrel | not source-reported | not source-reported | May 26, 2026 | FRED DCOILBRENTEU | observed |
| NATURAL_GAS | natural gas futures | 3.185 | USD per MMBtu | not source-reported | not source-reported | June 2, 2026 01:11:13 source time | Stooq NG.F Quote | observed |
| GOLD | gold futures | 4515.75 | USD per troy ounce | not source-reported | not source-reported | June 2, 2026 01:11:17 source time | Stooq GC.F Quote | observed |
| SILVER | silver futures | 7523.7 | US cents per troy ounce | not source-reported | not source-reported | June 2, 2026 01:11:10 source time | Stooq SI.F Quote | observed |
| COPPER | high grade copper futures | 656.68 | US cents per pound | not source-reported | not source-reported | June 2, 2026 01:09:59 source time | Stooq HG.F Quote | observed |
| BROAD_COMMODITY_INDEX | broad commodity index | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| US_DOLLAR_INDEX | U.S. Dollar Index futures | 99.142 | index | not source-reported | not source-reported | June 1, 2026 22:58:08 source time | Stooq DX.F Quote | observed |
| EURUSD | euro / U.S. dollar | 1.1635 | exchange rate | not source-reported | not source-reported | June 2, 2026 01:11:16 source time | Stooq EURUSD Quote | observed |
| USDJPY | U.S. dollar / Japanese yen | 159.6555 | exchange rate | not source-reported | not source-reported | June 2, 2026 01:11:16 source time | Stooq USDJPY Quote | observed |
| BITCOIN | bitcoin | 71324.85 | USD | not source-reported | not source-reported | June 2, 2026 01:11:20 source time | Stooq BTC.V Quote | observed |
| ETHEREUM | ethereum | 2002.575 | USD | not source-reported | not source-reported | June 2, 2026 01:11:20 source time | Stooq ETH.V Quote | observed |

## 6. Broad Equity Market Datapoints

| indicator_id | data_area | measure | latest_value | unit | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source | status |
|---|---|---|---:|---|---|---|---|---|---|---|
| SP500_INDEX_LEVEL | broad equity market | S&P 500 index close | 7600.00 | index | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 23:00:00 source time | Stooq ^SPX Quote | observed |
| NASDAQ_COMPOSITE_INDEX_LEVEL | broad equity market | Nasdaq Composite index close | 27086.81 | index | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 23:00:00 source time | Stooq ^NDQ Quote | observed |
| RUSSELL_2000_INDEX_LEVEL | broad equity market | Russell 2000 index close | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| SP500_FORWARD_PE_OR_CAPE | broad equity market | S&P 500 forward 12-month P/E | 25.9 | ratio | 5-year average of 21.4 and 10-year average of 19.3 | range or percentile explicitly reported by the source | as of May 29, 2026 | May 29, 2026 | FactSet Earnings Insight | observed |
| SP500_EARNINGS_GROWTH_ESTIMATE | broad equity market | S&P 500 estimated earnings growth rate | 9.4 | % | not source-reported | not source-reported | Q2 2026 estimate | May 29, 2026 | FactSet Earnings Insight | forecast_or_estimate |
| SP500_EARNINGS_REVISION_OR_BEAT_RATE | broad equity market | S&P 500 earnings revision or beat-rate datapoint | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| US_EQUITY_MARKET_BREADTH | broad equity market | broad equity market breadth datapoint | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| EQUAL_WEIGHT_VS_CAP_WEIGHT_CONTEXT | broad equity market | equal-weight versus cap-weight datapoint | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| EQUITY_PUT_CALL_RATIO | broad equity market | equity put/call ratio | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| INVESTOR_SENTIMENT_SURVEY | broad equity market | AAII investor sentiment survey, bull-bear spread | -6.3 | percentage points | historical average of +6.5 percentage points | range or percentile explicitly reported by the source | week ending May 27, 2026 | May 28, 2026 | AAII Investor Sentiment Survey | observed |
| US_EQUITY_FUND_FLOWS | broad equity market | U.S. equity fund flows | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| ETF_FUND_FLOWS_EQUITY_BOND_CASH | broad equity market | ETF fund flows across equity, bond, and cash categories | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| MARGIN_DEBT_OR_LEVERAGE_DATAPOINT | broad equity market | FINRA debit balances in customers' securities margin accounts | 987.8 | USD billions | not source-reported | not source-reported | April 2026 | May 2026 | FINRA Margin Statistics | observed |
| IMPLIED_CORRELATION_OR_REALIZED_CORRELATION | broad equity market | implied or realized correlation datapoint | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |

## 7. Scheduled Macro Events

| event_id | date | event | publisher_or_entity | release_type | consensus_or_forecast_if_source_reported | source | status |
|---|---|---|---|---|---|---|---|
| NEXT_CPI_RELEASE | June 10, 2026 8:30 AM ET | CPI, May 2026 | U.S. Bureau of Labor Statistics | inflation release | not source-reported | BLS Release Calendar | scheduled |
| NEXT_PCE_RELEASE | June 25, 2026 8:30 AM ET | Personal Income and Outlays, May 2026 | U.S. Bureau of Economic Analysis | inflation and income release | not source-reported | BEA Release Schedule | scheduled |
| NEXT_PPI_RELEASE | June 11, 2026 8:30 AM ET | Producer Price Index, May 2026 | U.S. Bureau of Labor Statistics | inflation release | not source-reported | BLS Release Calendar | scheduled |
| NEXT_EMPLOYMENT_REPORT | June 5, 2026 8:30 AM ET | Employment Situation, May 2026 | U.S. Bureau of Labor Statistics | labor market release | not source-reported | BLS Employment Situation | scheduled |
| NEXT_RETAIL_SALES_RELEASE | June 17, 2026 8:30 AM ET | Advance Monthly Sales for Retail and Food Services, May 2026 | U.S. Census Bureau | economic data release | not source-reported | U.S. Census Monthly Retail Trade | scheduled |
| NEXT_GDP_RELEASE | June 25, 2026 8:30 AM ET | Q1 2026 GDP third estimate | U.S. Bureau of Economic Analysis | economic data release | not source-reported | BEA Release Schedule | scheduled |
| NEXT_ISM_MANUFACTURING_RELEASE | July 1, 2026 10:00 AM ET | ISM Manufacturing PMI, June 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Manufacturing PMI | scheduled |
| NEXT_ISM_SERVICES_RELEASE | June 3, 2026 10:00 AM ET | ISM Services PMI, May 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar | scheduled |
| NEXT_FOMC_DECISION | June 16-17, 2026 | FOMC meeting | Federal Reserve | monetary policy decision | not source-reported | Federal Reserve FOMC Calendar | scheduled |
| NEXT_FOMC_MINUTES | outside scoring window | FOMC minutes | Federal Reserve | monetary policy minutes | not source-reported | Federal Reserve FOMC Calendar | outside_window |
| NEXT_TREASURY_REFUNDING_OR_MAJOR_AUCTION | not provided | Treasury refunding or major auction | U.S. Treasury | Treasury financing event | not provided | not provided | not_provided |
| NEXT_ECB_DECISION | June 11, 2026 | Governing Council monetary policy decision | European Central Bank | monetary policy decision | not source-reported | ECB Governing Council Calendar | scheduled |
| NEXT_BOJ_DECISION | June 16-17, 2026 | Monetary Policy Meeting | Bank of Japan | monetary policy decision | not source-reported | Bank of Japan MPM Schedule | scheduled |
| NEXT_BOE_DECISION | June 18, 2026 | Monetary Policy Committee decision | Bank of England | monetary policy decision | not source-reported | Bank of England Monetary Policy Committee dates | scheduled |
| NEXT_PBOC_LPR_FIXING | June 22, 2026 | Loan Prime Rate fixing | People's Bank of China and National Interbank Funding Center | policy-rate fixing | not source-reported | National Interbank Funding Center LPR | scheduled |
| NEXT_JOBLESS_CLAIMS_RELEASE | June 4, 2026 | Unemployment Insurance Weekly Claims | U.S. Department of Labor | labor market release | not source-reported | U.S. Department of Labor UI Claims | scheduled |
| NEXT_JOLTS_RELEASE | June 3, 2026 | Job Openings and Labor Turnover Survey, April 2026 | U.S. Bureau of Labor Statistics | labor market release | not source-reported | BLS JOLTS | scheduled |
| NEXT_DURABLE_GOODS_RELEASE | June 26, 2026 | Durable Goods Manufacturers' Shipments, Inventories, and Orders, May 2026 advance | U.S. Census Bureau | manufacturing release | not source-reported | Census Advance Report on Durable Goods | scheduled |
| NEXT_TRADE_BALANCE_RELEASE | June 4, 2026 8:30 AM ET | U.S. International Trade in Goods and Services, April 2026 | U.S. Census Bureau and Bureau of Economic Analysis | trade release | not source-reported | BEA Release Schedule | scheduled |
| NEXT_INDUSTRIAL_PRODUCTION_RELEASE | June 16, 2026 | Industrial Production and Capacity Utilization, May 2026 | Federal Reserve | production release | not source-reported | Federal Reserve Statistical Release Calendar | scheduled |
| NEXT_CONSUMER_SENTIMENT_RELEASE | June 13, 2026 | University of Michigan Consumer Sentiment, June 2026 preliminary | University of Michigan Surveys of Consumers | consumer survey release | not source-reported | University of Michigan Surveys of Consumers | scheduled |
| NEXT_CONSUMER_CONFIDENCE_RELEASE | June 24, 2026 | Consumer Confidence Index, June 2026 | The Conference Board | consumer survey release | not source-reported | The Conference Board Consumer Confidence | scheduled |
| NEXT_HOUSING_STARTS_RELEASE | June 16, 2026 | New Residential Construction, May 2026 | U.S. Census Bureau and HUD | housing release | not source-reported | Census/HUD New Residential Construction | scheduled |
| NEXT_EXISTING_HOME_SALES_RELEASE | June 9, 2026 | Existing-Home Sales, May 2026 | National Association of Realtors | housing release | not source-reported | NAR Existing-Home Sales | scheduled |
| NEXT_NEW_HOME_SALES_RELEASE | June 25, 2026 | New Residential Sales, May 2026 | U.S. Census Bureau and HUD | housing release | not source-reported | Census New Residential Sales | scheduled |
| NEXT_MAJOR_INDEX_EARNINGS_UPDATE | not provided | major index earnings update | not provided | earnings update | not provided | not provided | not_provided |

## 8. Fixed Asset-Area Datapoints

| row_id | asset_area | requested_datapoint | latest_value_or_fact | unit_if_applicable | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source | status |
|---|---|---|---|---|---|---|---|---|---|---|
| CASH_SHORT_TREASURY_POLICY_RATE | cash and short-duration Treasuries | current federal funds target range or nearest official short-rate policy setting | The FOMC maintained the federal funds target range at 3.50% to 3.75%. | % | not source-reported | not source-reported | current target range | April 29, 2026 | Federal Reserve FOMC Statement | policy_or_regulatory_fact |
| BROAD_US_EQUITIES_CORPORATE_PROFITS | broad US equities | latest official corporate profits or broad index earnings aggregate | Profits from current production increased $40.4 billion in Q1 2026. | USD billions | $246.9 billion increase in Q4 2025 | prior value | Q1 2026 second estimate | May 28, 2026 | BEA GDP Second Estimate | observed |
| BROAD_US_EQUITIES_GDP | broad US equities | latest real GDP growth value | Real GDP increased at a 1.6% annual rate in Q1 2026. | % QoQ SAAR | revised down 0.4 percentage point from the advance estimate; Q4 2025 was +0.5% | revision and prior value | Q1 2026 second estimate | May 28, 2026 | BEA GDP Second Estimate | observed |
| BROAD_US_EQUITIES_VALUATION | broad US equities | latest broad valuation datapoint such as forward P/E, CAPE, or earnings yield if source-reported | S&P 500 forward 12-month P/E was 25.9. | ratio | 5-year average of 21.4 and 10-year average of 19.3 | range or percentile explicitly reported by the source | as of May 29, 2026 | May 29, 2026 | FactSet Earnings Insight | observed |
| BROAD_US_EQUITIES_MARKET_BREADTH | broad US equities | latest broad market breadth datapoint if source-reported | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| NASDAQ_GROWTH_TECH_INDEX_OR_SECTOR_FACT | Nasdaq / growth / technology | latest broad technology sector or Nasdaq-level fact, not single-company news | Nasdaq Composite index close was 27,086.81. | index | not source-reported | not source-reported | June 1, 2026 | June 1, 2026 23:00:00 source time | Stooq ^NDQ Quote | observed |
| LARGE_GROWTH_CONTEXT | large-cap growth | latest broad large-growth style fact, valuation fact, earnings fact, or factor fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| LARGE_VALUE_CONTEXT | large-cap value | latest broad large-value style fact, valuation fact, earnings fact, or factor fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| MID_CAP_CONTEXT | mid-cap equities | latest broad mid-cap index, earnings, financing, or domestic-growth fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| SMALL_CAP_CONTEXT | small-cap equities | latest broad small-cap index, earnings, financing, or domestic-growth fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| SMALL_VALUE_CONTEXT | small-cap value | latest broad small-value style, valuation, earnings, or financing fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| DIVIDEND_CONTEXT | dividend equities | latest broad dividend-yield, payout, dividend-growth, or factor fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| LOW_VOLATILITY_CONTEXT | low-volatility equities | latest broad low-volatility factor, realized volatility, low-beta factor, or minimum-volatility factor fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| MOMENTUM_CONTEXT | momentum equities | latest broad momentum factor, factor rotation, or style-index fact from a reliable source | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| COMMUNICATION_SERVICES_CONTEXT | communication services | latest broad sector fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| CONSUMER_DISCRETIONARY_CONTEXT | consumer discretionary | latest broad sector fact or consumer spending datapoint | Current-dollar personal consumption expenditures increased $111.1 billion, or 0.5%. | USD billions and % MoM | 1.0% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| CONSUMER_STAPLES_CONTEXT | consumer staples | latest broad sector fact or consumer spending/inflation datapoint | The PCE price index increased 0.4% in April 2026. | % MoM | 0.7% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays | observed |
| HEALTHCARE_CONTEXT | healthcare | latest broad sector, policy, or spending fact | CMS published the selected-drug list and negotiated prices file for Medicare maximum fair prices. | text | not source-reported | not source-reported | current as of source page | May 26, 2026 | CMS Medicare Drug Price Negotiation Program | policy_or_regulatory_fact |
| BIOTECH_CONTEXT | biotechnology | latest broad biotech industry, policy, or index-level fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| FINANCIALS_CONTEXT | financials | latest broad banking, credit, or financial-sector fact | FDIC-insured institutions reported a 1.26% return on assets ratio and $80.5 billion of aggregate net income. | % and USD billions | net income increased $2.8 billion, or 3.6%, from the prior quarter | prior value | Q1 2026 | May 2026 | FDIC Quarterly Banking Profile | observed |
| REGIONAL_BANKS_CONTEXT | regional banks | latest regional-bank industry, FDIC, credit, or deposit fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| INDUSTRIALS_CONTEXT | industrials | latest industrial production, manufacturing, or broad sector fact | ISM Manufacturing PMI registered 54.0 in May 2026. | index | 52.7 in April 2026; up 1.3 percentage points | prior value and month-over-month change | May 2026 | June 1, 2026 | ISM Manufacturing PMI | observed |
| AEROSPACE_DEFENSE_CONTEXT | aerospace and defense | latest broad defense budget, orders, production, or policy fact | The FY2027 U.S. defense budget request totaled $1.5 trillion, including a $1.15 trillion base request and $350 billion from reconciliation. | USD trillions and USD billions | not source-reported | not source-reported | April 2026 | April 2026 | Breaking Defense | policy_or_regulatory_fact |
| ENERGY_CONTEXT | energy | latest broad energy-sector, oil/gas supply, or inventory fact | EIA forecast global oil inventories would decrease by 2.6 million barrels per day in 2026. | million barrels per day | prior STEO forecast a 0.3 million barrel per day decrease | prior value | May 2026 Short-Term Energy Outlook | May 2026 | EIA STEO | forecast_or_estimate |
| MATERIALS_CONTEXT | materials | latest broad materials, chemicals, or industrial-input fact | Producer Price Index for final demand increased 1.4% in April 2026. | % MoM | 0.7% in March 2026 and 0.6% in February 2026 | prior value | April 2026 | May 13, 2026 | BLS Producer Price Index | observed |
| METALS_MINING_CONTEXT | metals and mining | latest broad metals/mining production, price, inventory, or forecast fact | The World Bank said average base-metals prices were projected to reach all-time highs. | text | not source-reported | not source-reported | April 2026 Commodity Markets Outlook | April 28, 2026 | World Bank Commodity Markets Outlook | forecast_or_estimate |
| UTILITIES_CONTEXT | utilities | latest electricity demand, generation, rate, or broad utility-sector fact | EIA forecast U.S. electricity demand would rise 1.3% in 2026, average almost 4,250 billion kilowatthours, and grow another 3.1% in 2027. | %, billion kilowatthours | not source-reported | not source-reported | May 2026 Short-Term Energy Outlook | May 2026 | EIA STEO | forecast_or_estimate |
| REAL_ESTATE_CONTEXT | real estate | latest housing, REIT, mortgage, or property-market fact | Housing starts were 1,465,000 SAAR, and building permits were 1,442,000 SAAR. | SAAR | starts down 2.8%; permits up 5.8% from March 2026 | month-over-month change | April 2026 | May 21, 2026 | Census/HUD New Residential Construction | observed |
| INTERMEDIATE_TREASURY_CONTEXT | intermediate Treasuries | latest Treasury yield or policy fact from macro packet if no separate broad source exists | The 5-year Treasury constant maturity rate was 4.13%. | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS5 | observed |
| LONG_TREASURY_CONTEXT | long Treasuries | latest long-term Treasury yield or policy fact from macro packet if no separate broad source exists | The 30-year Treasury constant maturity rate was 4.99%. | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DGS30 | observed |
| TIPS_CONTEXT | TIPS | latest real yield or inflation-expectation fact | The 10-year Treasury inflation-indexed security constant maturity rate was 2.07%. | % | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 | FRED DFII10 | observed |
| AGGREGATE_BONDS_CONTEXT | aggregate bonds | latest aggregate bond-market yield, duration, or broad fixed-income fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| MBS_CONTEXT | agency mortgage-backed bonds | latest mortgage-rate or agency MBS market fact | The 30-year fixed-rate mortgage average was 6.53%. | % | 6.51% previous week | prior value | week ending May 28, 2026 | May 28, 2026 | FRED MORTGAGE30US | observed |
| MUNICIPAL_BONDS_CONTEXT | municipal bonds | latest municipal bond yield, issuance, credit, or fund-flow fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| INVESTMENT_GRADE_CREDIT_CONTEXT | investment-grade credit | latest investment-grade credit spread or broad corporate credit fact | ICE BofA US Corporate Index option-adjusted spread was 0.74%. | % | not source-reported | not source-reported | May 31, 2026 | May 31, 2026 | FRED BAMLC0A0CM | observed |
| HIGH_YIELD_CREDIT_CONTEXT | high-yield credit | latest high-yield credit spread or default/fund-flow fact | ICE BofA US High Yield Index option-adjusted spread was 2.74%. | % | not source-reported | not source-reported | May 31, 2026 | May 31, 2026 | FRED BAMLH0A0HYM2 | observed |
| EMERGING_MARKET_BONDS_CONTEXT | emerging-market bonds | latest EM bond spread, yield, flow, or debt fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| INTERNATIONAL_BONDS_CONTEXT | international aggregate bonds | latest non-US aggregate bond yield, hedged global bond, currency-hedging, or international rates fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| DEVELOPED_EX_US_CONTEXT | developed ex-US equities | latest developed-market ex-US or MSCI/EAFE-level fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| EMERGING_MARKETS_CONTEXT | emerging-market equities | latest broad emerging-market equity, GDP, PMI, flows, currency, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| EUROPE_CONTEXT | Europe equities | latest ECB, euro area GDP, inflation, PMI, or policy fact | The ECB held the deposit facility, main refinancing operations, and marginal lending facility rates at 2.00%, 2.15%, and 2.40%, respectively. | % | not source-reported | not source-reported | April 30, 2026 monetary policy decision | April 30, 2026 | European Central Bank | policy_or_regulatory_fact |
| JAPAN_CONTEXT | Japan equities | latest BOJ, Japan GDP, inflation, PMI, or policy fact | The Bank of Japan encouraged the uncollateralized overnight call rate to remain at around 0.75%. | % | not source-reported | not source-reported | April 2026 monetary policy meeting | April 28, 2026 | Bank of Japan Monetary Policy Statement | policy_or_regulatory_fact |
| CHINA_CONTEXT | China equities | latest China GDP, PMI, LPR, inflation, trade, or policy fact | China's one-year Loan Prime Rate was 3.0%, and its five-year Loan Prime Rate was 3.5%; China's official manufacturing PMI was 50.3 in April 2026. | % and index | manufacturing PMI down 0.1 percentage point from the previous month | month-over-month change | May 2026 LPR; April 2026 PMI | May 2026 | Trading Economics China Interest Rate ; National Bureau of Statistics of China PMI | observed |
| INDIA_CONTEXT | India equities | latest India GDP, CPI, RBI, PMI, or policy fact | India's April 2026 CPI inflation was 3.48%, and the Reserve Bank of India policy repo rate was 5.25%. | % | CPI was 3.40% in March 2026 | prior value | April 2026 CPI; April 2026 monetary policy | May 2026 | Press Information Bureau India CPI ; Reserve Bank of India Current Rates | observed |
| CANADA_CONTEXT | Canada equities | latest Bank of Canada, GDP, CPI, commodity, or policy fact | The Bank of Canada held its target for the overnight rate at 2.25%, with the Bank Rate at 2.50% and the deposit rate at 2.20%. | % | not source-reported | not source-reported | April 29, 2026 policy decision | April 29, 2026 | Bank of Canada | policy_or_regulatory_fact |
| UK_CONTEXT | UK equities | latest Bank of England, GDP, CPI, PMI, or policy fact | The Bank of England MPC voted 8-1 to maintain Bank Rate at 3.75%. | % | not source-reported | not source-reported | April 2026 meeting | April 29, 2026 | Bank of England Monetary Policy Summary | policy_or_regulatory_fact |
| AUSTRALIA_CONTEXT | Australia equities | latest RBA, GDP, CPI, commodity, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| SOUTH_KOREA_CONTEXT | South Korea equities | latest Korea GDP, exports, CPI, Bank of Korea, semiconductor export, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| TAIWAN_CONTEXT | Taiwan equities | latest Taiwan GDP, exports, inflation, central-bank, semiconductor export, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| BRAZIL_CONTEXT | Brazil equities | latest Brazil GDP, inflation, central-bank, commodity, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| MEXICO_CONTEXT | Mexico equities | latest Mexico GDP, inflation, central-bank, trade, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| SOUTH_AFRICA_CONTEXT | South Africa equities | latest South Africa GDP, inflation, central-bank, commodity, or policy fact | not provided | not provided | not provided | not provided | not provided | not provided | not provided | not_provided |
| GOLD_CONTEXT | gold | latest broad gold price, demand, central-bank purchases, or forecast fact | Gold futures were quoted at $4,524.76 per troy ounce. | USD per troy ounce | not source-reported | not source-reported | June 2, 2026 05:28:13 source time | June 2, 2026 05:28:13 source time | Stooq GC.F Quote | observed |
| SILVER_CONTEXT | silver | latest broad silver price, demand, supply, or forecast fact | The Silver Institute said the silver market was expected to remain in deficit for a sixth consecutive year in 2026. | text | total global silver supply forecast to increase by 1.5% to 1.05 billion ounces | consensus / forecast comparison | 2026 forecast | February 10, 2026 | The Silver Institute | forecast_or_estimate |
| COPPER_CONTEXT | copper | latest broad copper price, inventory, demand, supply, or forecast fact | High grade copper futures were quoted at 656.4 US cents per pound. | US cents per pound | not source-reported | not source-reported | June 2, 2026 05:28:14 source time | June 2, 2026 05:28:14 source time | Stooq HG.F Quote | observed |
| AGRICULTURE_CONTEXT | agriculture | latest broad agriculture price, crop, WASDE, or supply fact | USDA forecast the U.S. corn crop at 16.0 billion bushels for 2026/27. | billion bushels | down 6% from a year ago | year-over-year change | 2026/27 marketing year forecast | May 2026 WASDE | USDA WASDE | forecast_or_estimate |
| BROAD_COMMODITIES_CONTEXT | broad commodities | latest broad commodity index, World Bank, or commodity-market fact | The World Bank forecast overall commodity prices to increase 16% in 2026. | % | not source-reported | not source-reported | April 2026 Commodity Markets Outlook | April 28, 2026 | World Bank Commodity Markets Outlook | forecast_or_estimate |
| OIL_CONTEXT | oil | latest oil price, inventory, OPEC, EIA, supply, or demand fact | WTI crude futures were quoted at $91.64 per barrel. | USD per barrel | not source-reported | not source-reported | June 2, 2026 05:28:09 source time | June 2, 2026 05:28:09 source time | Stooq CL.F Quote | observed |
| US_DOLLAR_CONTEXT | US dollar | latest DXY or broad dollar fact | U.S. Dollar Index futures were quoted at 99.15. | index | not source-reported | not source-reported | June 2, 2026 05:28:12 source time | June 2, 2026 05:28:12 source time | Stooq DX.F Quote | observed |
| EURO_CONTEXT | euro | latest ECB, EUR/USD, euro-area rate, or currency fact | EUR/USD was quoted at 1.16326. | exchange rate | not source-reported | not source-reported | June 2, 2026 05:28:12 source time | June 2, 2026 05:28:12 source time | Stooq EURUSD Quote | observed |
| YEN_CONTEXT | yen | latest BOJ, USD/JPY, Japan rate, or currency fact | USD/JPY was quoted at 159.7135. | exchange rate | not source-reported | not source-reported | June 2, 2026 05:28:12 source time | June 2, 2026 05:28:12 source time | Stooq USDJPY Quote | observed |
| BITCOIN_CONTEXT | bitcoin proxy | latest bitcoin price, ETF flow, regulatory, or market-structure fact | Bitcoin was quoted at $70,869.54. | USD | not source-reported | not source-reported | June 2, 2026 05:28:16 source time | June 2, 2026 05:28:16 source time | Stooq BTC.V Quote | observed |
| ETHEREUM_CONTEXT | ethereum proxy | latest ethereum price, ETF flow, regulatory, or market-structure fact | Ethereum was quoted at $1,997.419. | USD | not source-reported | not source-reported | June 2, 2026 05:28:12 source time | June 2, 2026 05:28:12 source time | Stooq ETH.V Quote | observed |
| SEMICONDUCTORS_CONTEXT | semiconductors | latest global semiconductor sales, industry shipment, equipment, export, or broad supply-chain fact | Global semiconductor sales were $298.5 billion during Q1 2026. | USD billions | up 25% compared to Q4 2025 | prior value | Q1 2026 | May 2026 | Semiconductor Industry Association | observed |
| SOFTWARE_CONTEXT | software | latest broad software price, spending, revenue, or sector fact | The PCE Computer Software and Accessories category increased 13.9% year over year and roughly 73.1% annualized from November 2025 through March 2026. | % YoY and % annualized | average annualized rate of -5.3% over the prior 25 years | prior value | November 2025 through March 2026 | May 22, 2026 | Federal Reserve FEDS Notes | observed |
| BROAD_AI_TECH_CONTEXT | broad AI technology | latest broad AI spending, investment, infrastructure, or policy fact | Gartner forecast worldwide AI spending to total $2.59 trillion in 2026. | USD trillions | 47% increase year over year | year-over-year change | 2026 forecast | May 2026 | Business Wire / Gartner | forecast_or_estimate |
| AUTONOMOUS_ROBOTICS_CONTEXT | autonomous technology / robotics | latest robotics order, automation, industrial robot, or policy fact | North American companies ordered 9,055 robots valued at $543 million in Q1 2026. | robot units and USD millions | units decreased 0.1% and revenue declined 6.4% year over year | year-over-year change | Q1 2026 | May 2026 | Business Wire / Association for Advancing Automation | observed |
| CYBERSECURITY_CONTEXT | cybersecurity | latest broad cybersecurity spending, incident count, policy, or sector fact | Gartner listed AI cybersecurity spending of $85.997 billion in 2026 in its worldwide AI spending forecast. | USD billions | $51.347 billion in 2025 | prior value | 2026 forecast | May 2026 | Business Wire / Gartner | forecast_or_estimate |
| AI_INFRASTRUCTURE_CONTEXT | AI infrastructure | latest data-center, power demand, capex, chips, cloud infrastructure, or policy fact | IEA reported capital expenditure of five large technology companies was more than $400 billion in 2025. | USD billions | set to increase by a further 75% in 2026 | consensus / forecast comparison | 2025 and 2026 forecast | April 16, 2026 | IEA Energy and AI | forecast_or_estimate |
| SOLAR_CONTEXT | solar | latest solar generation, installation, capacity, policy, or forecast fact | EIA said its utility-scale solar generation forecast for 2026 was 1.4% higher than in the previous STEO. | % revision | 1.4% higher than previous STEO | revision | May 2026 Short-Term Energy Outlook | May 2026 | EIA STEO | forecast_or_estimate |

## 9. Scheduled Asset-Area Events

| event_id | date | asset_area | event | entity_or_publisher | source | status |
|---|---|---|---|---|---|---|
| NEXT_MAJOR_CENTRAL_BANK_EVENTS | June 11, 2026; June 16-17, 2026; June 18, 2026; June 22, 2026 | Europe equities; Japan equities; UK equities; China equities; bonds and rates; currencies | ECB, FOMC, BOJ, BOE, and PBOC policy events | European Central Bank; Federal Reserve; Bank of Japan; Bank of England; People's Bank of China / National Interbank Funding Center | ECB Governing Council Calendar ; Federal Reserve FOMC Calendar ; Bank of Japan MPM Schedule ; Bank of England MPC Dates ; National Interbank Funding Center LPR | scheduled |
| NEXT_MAJOR_COUNTRY_INFLATION_RELEASES | June 10-11, 2026 | bonds and rates; TIPS; broad US equities; materials | U.S. CPI and PPI, May 2026 | U.S. Bureau of Labor Statistics | BLS Release Calendar | scheduled |
| NEXT_MAJOR_COUNTRY_GDP_RELEASES | June 25, 2026 8:30 AM ET | broad US equities | Q1 2026 GDP third estimate | U.S. Bureau of Economic Analysis | BEA Release Schedule | scheduled |
| NEXT_MAJOR_COUNTRY_PMI_RELEASES | June 3, 2026 10:00 AM ET; July 1, 2026 10:00 AM ET | broad US equities; consumer sectors; industrials | ISM Services PMI, May 2026; ISM Manufacturing PMI, June 2026 | Institute for Supply Management | ISM Report Calendar ; ISM Manufacturing PMI | scheduled |
| NEXT_MAJOR_COMMODITY_POLICY_OR_INVENTORY_EVENTS | June 4, 2026; June 9, 2026 | energy; oil; broad commodities | Weekly Petroleum Status Report and Short-Term Energy Outlook | U.S. Energy Information Administration | EIA Weekly Petroleum Status Report ; EIA STEO | scheduled |
| NEXT_MAJOR_ENERGY_REPORTS | June 5, 2026; June 9, 2026 | energy; oil | North America Rotary Rig Count and Short-Term Energy Outlook | Baker Hughes; U.S. Energy Information Administration | Baker Hughes Rig Count ; EIA STEO | scheduled |
| NEXT_MAJOR_TREASURY_OR_CREDIT_EVENTS | not scheduled inside scoring window | not provided | not provided | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_BROAD_INDEX_EARNINGS_MILESTONE | not scheduled inside scoring window | not provided | not provided | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_SECTOR_POLICY_EVENTS | not scheduled inside scoring window | not provided | not provided | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_CRYPTO_REGULATORY_OR_ETF_EVENTS | not scheduled inside scoring window | not provided | not provided | not provided | not provided | not_scheduled_inside_window |

## 10. Missing Or Limited Datapoints

### Macro Missing Datapoints

| section | indicator_or_event_id | missing_item | note |
|---|---|---|---|
| Section 2 | PCE_GOODS_MOM | PCE goods price index MoM | not provided in source reports |
| Section 2 | PCE_SERVICES_MOM | PCE services price index MoM | not provided in source reports |
| Section 2 | RETAIL_SALES_CONTROL_GROUP_MOM | retail sales control group MoM | not provided in source reports |
| Section 2 | CONSUMER_INFLATION_EXPECTATIONS_5Y | consumer inflation expectations 5 to 10 years | not provided in source reports |
| Section 2 | PENDING_HOME_SALES | pending home sales index | not provided in source reports |
| Section 3 | INFLATION_SWAP_OR_MARKET_EXPECTATION_1Y | 1-year market inflation expectation | not provided in source reports |
| Section 3 | MOVE_INDEX | ICE BofA MOVE Index | not provided in source reports |
| Section 4 | BROAD_COMMODITY_INDEX | broad commodity index | not provided in source reports |
| Section 5 | RUSSELL_2000_INDEX_LEVEL | Russell 2000 index level | not provided in source reports |
| Section 5 | SP500_EARNINGS_REVISION_OR_BEAT_RATE | S&P 500 earnings revision or beat-rate datapoint | not provided in source reports |
| Section 5 | US_EQUITY_MARKET_BREADTH | broad equity market breadth datapoint | not provided in source reports |
| Section 5 | EQUAL_WEIGHT_VS_CAP_WEIGHT_CONTEXT | equal-weight versus cap-weight datapoint | not provided in source reports |
| Section 5 | EQUITY_PUT_CALL_RATIO | equity put/call ratio | not provided in source reports |
| Section 5 | US_EQUITY_FUND_FLOWS | U.S. equity fund flows | not provided in source reports |
| Section 5 | ETF_FUND_FLOWS_EQUITY_BOND_CASH | ETF fund flows across equity, bond, and cash categories | not provided in source reports |
| Section 5 | IMPLIED_CORRELATION_OR_REALIZED_CORRELATION | implied or realized correlation datapoint | not provided in source reports |
| Section 6 | NEXT_FOMC_MINUTES | FOMC minutes | outside scoring window |
| Section 6 | NEXT_TREASURY_REFUNDING_OR_MAJOR_AUCTION | Treasury refunding or major auction | not provided in source reports |
| Section 6 | NEXT_MAJOR_INDEX_EARNINGS_UPDATE | major index earnings update | not provided in source reports |

### Asset-Area Missing Or Limited Datapoints

| section | row_or_event_id | asset_area | missing_or_limited_item | note |
|---|---|---|---|---|
| Section 2 | BROAD_US_EQUITIES_MARKET_BREADTH | broad US equities | latest broad market breadth datapoint | not provided in source reports |
| Section 2 | LARGE_GROWTH_CONTEXT | large-cap growth | latest broad large-growth style fact, valuation fact, earnings fact, or factor fact | not provided in source reports |
| Section 2 | LARGE_VALUE_CONTEXT | large-cap value | latest broad large-value style fact, valuation fact, earnings fact, or factor fact | not provided in source reports |
| Section 2 | MID_CAP_CONTEXT | mid-cap equities | latest broad mid-cap index, earnings, financing, or domestic-growth fact | not provided in source reports |
| Section 2 | SMALL_CAP_CONTEXT | small-cap equities | latest broad small-cap index, earnings, financing, or domestic-growth fact | not provided in source reports |
| Section 2 | SMALL_VALUE_CONTEXT | small-cap value | latest broad small-value style, valuation, earnings, or financing fact | not provided in source reports |
| Section 2 | DIVIDEND_CONTEXT | dividend equities | latest broad dividend-yield, payout, dividend-growth, or factor fact | not provided in source reports |
| Section 2 | LOW_VOLATILITY_CONTEXT | low-volatility equities | latest broad low-volatility factor, realized volatility, low-beta factor, or minimum-volatility factor fact | not provided in source reports |
| Section 2 | MOMENTUM_CONTEXT | momentum equities | latest broad momentum factor, factor rotation, or style-index fact from a reliable source | not provided in source reports |
| Section 2 | COMMUNICATION_SERVICES_CONTEXT | communication services | latest broad sector fact | not provided in source reports |
| Section 2 | BIOTECH_CONTEXT | biotechnology | latest broad biotech industry, policy, or index-level fact | not provided in source reports |
| Section 2 | REGIONAL_BANKS_CONTEXT | regional banks | latest regional-bank industry, FDIC, credit, or deposit fact | not provided in source reports |
| Section 2 | AGGREGATE_BONDS_CONTEXT | aggregate bonds | latest aggregate bond-market yield, duration, or broad fixed-income fact | not provided in source reports |
| Section 2 | MUNICIPAL_BONDS_CONTEXT | municipal bonds | latest municipal bond yield, issuance, credit, or fund-flow fact | not provided in source reports |
| Section 2 | EMERGING_MARKET_BONDS_CONTEXT | emerging-market bonds | latest EM bond spread, yield, flow, or debt fact | not provided in source reports |
| Section 2 | INTERNATIONAL_BONDS_CONTEXT | international aggregate bonds | latest non-US aggregate bond yield, hedged global bond, currency-hedging, or international rates fact | not provided in source reports |
| Section 2 | DEVELOPED_EX_US_CONTEXT | developed ex-US equities | latest developed-market ex-US or MSCI/EAFE-level fact | not provided in source reports |
| Section 2 | EMERGING_MARKETS_CONTEXT | emerging-market equities | latest broad emerging-market equity, GDP, PMI, flows, currency, or policy fact | not provided in source reports |
| Section 2 | AUSTRALIA_CONTEXT | Australia equities | latest RBA, GDP, CPI, commodity, or policy fact | not provided in source reports |
| Section 2 | SOUTH_KOREA_CONTEXT | South Korea equities | latest Korea GDP, exports, CPI, Bank of Korea, semiconductor export, or policy fact | not provided in source reports |
| Section 2 | TAIWAN_CONTEXT | Taiwan equities | latest Taiwan GDP, exports, inflation, central-bank, semiconductor export, or policy fact | not provided in source reports |
| Section 2 | BRAZIL_CONTEXT | Brazil equities | latest Brazil GDP, inflation, central-bank, commodity, or policy fact | not provided in source reports |
| Section 2 | MEXICO_CONTEXT | Mexico equities | latest Mexico GDP, inflation, central-bank, trade, or policy fact | not provided in source reports |
| Section 2 | SOUTH_AFRICA_CONTEXT | South Africa equities | latest South Africa GDP, inflation, central-bank, commodity, or policy fact | not provided in source reports |
| Section 3 | NEXT_MAJOR_TREASURY_OR_CREDIT_EVENTS | not provided | major Treasury or credit event | not scheduled inside scoring window |
| Section 3 | NEXT_MAJOR_BROAD_INDEX_EARNINGS_MILESTONE | not provided | major broad-index earnings milestone | not scheduled inside scoring window |
| Section 3 | NEXT_MAJOR_SECTOR_POLICY_EVENTS | not provided | major sector policy event | not scheduled inside scoring window |
| Section 3 | NEXT_MAJOR_CRYPTO_REGULATORY_OR_ETF_EVENTS | not provided | major crypto regulatory or ETF event | not scheduled inside scoring window |

## 11. Full-Universe Trailing Returns

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-01 | 0.00% | 0.00% | 0.00% | 0.00% | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-01 | 0.09% | 0.29% | 1.80% | 3.90% | pass |
| SP500 | SPY | us_broad_market | 2026-06-01 | 1.73% | 5.26% | 12.14% | 30.18% | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-01 | 1.80% | 5.10% | 12.25% | 30.34% | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-01 | 3.51% | 10.17% | 20.65% | 43.77% | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-01 | 3.02% | 7.26% | 8.68% | 29.44% | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-01 | 0.48% | 2.86% | 14.85% | 28.11% | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-01 | 1.41% | 2.38% | 13.83% | 25.85% | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-01 | 1.35% | 3.47% | 18.26% | 42.43% | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-01 | 0.68% | 2.17% | 18.52% | 43.56% | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-01 | -1.98% | 1.00% | 19.06% | 27.71% | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-01 | -3.75% | -3.66% | -0.23% | -0.80% | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-01 | 4.39% | 11.17% | 28.44% | 37.98% | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-01 | 8.52% | 20.94% | 37.10% | 70.51% | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-01 | 0.13% | -0.95% | 1.31% | 15.42% | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-01 | -0.83% | -0.37% | 0.30% | 11.42% | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-01 | -3.27% | -2.54% | 4.87% | 1.77% | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-01 | -1.37% | 1.85% | -4.00% | 13.44% | pass |
| FINANCIALS | XLF | us_sector | 2026-06-01 | -0.98% | -0.94% | -1.93% | 2.47% | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-01 | 0.37% | -0.32% | 14.54% | 22.32% | pass |
| ENERGY | XLE | us_sector | 2026-06-01 | -3.68% | -2.63% | 27.37% | 45.08% | pass |
| MATERIALS | XLB | us_sector | 2026-06-01 | 1.25% | -0.84% | 15.28% | 20.24% | pass |
| UTILITIES | XLU | us_sector | 2026-06-01 | -4.96% | -7.41% | -1.20% | 8.19% | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-01 | -2.89% | -2.37% | 7.16% | 7.27% | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-01 | 0.65% | -0.27% | -0.70% | 3.80% | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-01 | 1.33% | 0.23% | -1.51% | 3.97% | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-01 | 0.80% | -0.08% | 1.51% | 4.71% | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-01 | 0.90% | 0.68% | 0.54% | 6.13% | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-01 | 0.42% | 0.24% | 2.21% | 6.91% | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-01 | 0.58% | 0.11% | 0.59% | 4.98% | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-01 | 2.00% | 4.58% | 19.50% | 33.41% | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-01 | 2.44% | 2.42% | 13.54% | 32.12% | pass |
| EUROPE | VGK | international_equity | 2026-06-01 | 0.07% | 1.57% | 10.68% | 19.01% | pass |
| JAPAN | EWJ | international_equity | 2026-06-01 | 1.44% | 5.24% | 16.87% | 31.18% | pass |
| CHINA | MCHI | international_equity | 2026-06-01 | -0.25% | -4.02% | -10.50% | 7.21% | pass |
| INDIA | INDA | international_equity | 2026-06-01 | -0.83% | -2.30% | -11.67% | -11.64% | pass |
| GOLD | IAU | commodities | 2026-06-01 | -0.64% | -2.83% | 5.59% | 35.57% | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-01 | -1.81% | -2.72% | 34.85% | 47.97% | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-01 | 5.46% | 19.22% | 72.73% | 154.30% | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-01 | 14.56% | 24.32% | 3.49% | 3.91% | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-01 | 10.56% | 22.21% | 38.64% | 72.65% | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-01 | 2.67% | 8.62% | 29.26% | 76.33% | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-01 | 11.71% | 36.93% | 29.94% | 31.85% | pass |
| SOLAR | TAN | clean_energy | 2026-06-01 | 7.85% | 20.01% | 49.31% | 119.88% | pass |
| METALS_MINING | XME | commodities | 2026-06-01 | 8.88% | 7.51% | 33.27% | 112.99% | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-01 | 1.27% | 3.15% | 10.88% | 20.56% | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-01 | 1.49% | 2.45% | 11.85% | 69.34% | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-01 | -1.53% | -2.16% | 8.56% | 23.12% | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-01 | 2.01% | 6.31% | 15.47% | 30.41% | pass |
| CANADA | EWC | country_equity | 2026-06-01 | 0.34% | 0.53% | 13.52% | 32.63% | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-01 | -0.85% | -0.70% | 10.87% | 21.67% | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-01 | 1.22% | -0.48% | 15.16% | 16.55% | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-01 | 19.05% | 33.77% | 144.57% | 265.55% | pass |
| TAIWAN | EWT | country_equity | 2026-06-01 | 9.89% | 18.28% | 73.59% | 112.53% | pass |
| BRAZIL | EWZ | country_equity | 2026-06-01 | -1.92% | -9.54% | 10.63% | 38.27% | pass |
| MEXICO | EWW | country_equity | 2026-06-01 | 0.14% | 1.58% | 15.96% | 34.32% | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-01 | 0.46% | -0.85% | 5.76% | 38.25% | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-01 | 0.61% | 0.16% | 1.31% | 6.59% | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-01 | 0.99% | 0.38% | 1.67% | 6.60% | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-01 | 1.31% | 0.89% | 2.60% | 12.01% | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-01 | 0.34% | 0.53% | 0.50% | 1.90% | pass |
| SILVER | SLV | commodities | 2026-06-01 | -1.01% | -0.91% | 28.85% | 125.57% | pass |
| COPPER | CPER | commodities | 2026-06-01 | 2.67% | 10.30% | 23.75% | 36.10% | pass |
| AGRICULTURE | DBA | commodities | 2026-06-01 | -1.16% | -3.09% | 7.33% | 5.68% | pass |
| OIL | USO | commodities | 2026-06-01 | -3.85% | -5.11% | 90.68% | 101.79% | pass |
| US_DOLLAR | UUP | currencies | 2026-06-01 | -0.04% | 1.28% | 1.82% | 4.60% | pass |
| EURO | FXE | currencies | 2026-06-01 | 0.28% | -0.66% | 0.61% | 3.17% | pass |
| YEN | FXY | currencies | 2026-06-01 | -0.33% | -1.59% | -2.85% | -10.18% | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-01 | -5.75% | -8.95% | -16.52% | -31.90% | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-01 | -2.95% | -13.26% | -27.25% | -22.47% | pass |

## 12. Final Neutrality Statement

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Missing rows are preserved for comparability; inclusion, order, grouping, and row count are not evidence of expected return.

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
ID: BROAD_AI_TECH
Name: Broad AI Technology
Symbol: AIQ
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: very_high
Description: Broad artificial intelligence and technology equity exposure. Includes companies associated with AI applications, infrastructure, data, and related technology services.

Allowed option:
ID: AUTONOMOUS_ROBOTICS
Name: Autonomous Technology and Robotics
Symbol: ARKQ
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: very_high
Description: Autonomous technology and robotics equity exposure. Includes companies associated with automation, robotics, autonomous transport, energy storage, and related technology platforms.

Allowed option:
ID: CYBERSECURITY
Name: Cybersecurity
Symbol: CIBR
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: high
Description: Cybersecurity equity exposure. Includes companies providing network security, identity, endpoint, cloud security, and related cybersecurity products and services.

Allowed option:
ID: SOLAR
Name: Solar Energy
Symbol: TAN
Asset class: equity
Category: thematic_equity
Group: clean_energy
Risk bucket: very_high
Description: Solar energy equity exposure. Includes companies associated with solar power equipment, development, installation, and related clean-energy supply chains.

Allowed option:
ID: METALS_MINING
Name: Metals and Mining
Symbol: XME
Asset class: equity
Category: commodity_equity
Group: commodities
Risk bucket: very_high
Description: Metals and mining equity exposure. Includes companies involved in steel, aluminum, precious metals, coal, copper, and diversified mining industries.

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
