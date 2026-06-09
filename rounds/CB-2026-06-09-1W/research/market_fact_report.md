# Macro Datapoint Packet For CapitalBench

## 1. Research Setup

| field | value |
|---|---|
| decision_deadline | 2026-06-09T23:30:00Z |
| round_horizon | ONE WEEK |
| exit_date | 2026-06-16 |
| source_collection_rule | latest available information at research run time |

## 2. Core Macro Datapoints

| indicator_id                | data_area         | measure                        | latest_value | unit    | source_reported_comparison | comparison_type    | period_covered | release_or_observation_date | source                                                                          | status      |
|-----------------------------|-------------------|--------------------------------|--------------|---------|----------------------------|--------------------|----------------|-----------------------------|--------------------------------------------------------------------------------|-------------|
| CPI_HEADLINE_MOM            | CPI               | percent change (MoM)           | 0.6          | percent | 0.9                        | month-over-month   | Apr 2026       | 2026-05-12                  | BLS (CPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/cpi_05122026.htm#:~:text=The%20Consumer%20Price%20Index%20for,8%20percent%20before%20seasonal%20adjustment))                                     | observed    |
| CPI_HEADLINE_YOY            | CPI               | percent change (YoY)           | 3.8          | percent | 3.3                        | year-over-year     | Apr 2026       | 2026-05-12                  | BLS (CPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/cpi_05122026.htm#:~:text=reported%20today,8%20percent%20before%20seasonal%20adjustment))                                     | observed    |
| CPI_CORE_MOM                | CPI               | percent change (MoM)           | 0.4          | percent | 0.2                        | month-over-month   | Apr 2026       | 2026-05-12                  | BLS (CPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/cpi_05122026.htm#:~:text=The%20index%20for%20all%20items,Conversely%2C%20the%20indexes%20for))                                     | observed    |
| CPI_CORE_YOY                | CPI               | percent change (YoY)           | 2.8          | percent | 2.6                        | year-over-year     | Apr 2026       | 2026-05-12                  | BLS (CPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/cpi_05122026.htm#:~:text=The%20index%20for%20all%20items,5%20percent))                                    | observed    |
| CPI_SHELTER_MOM            | CPI               | percent change (MoM)           | 0.6          | percent | not provided              | not source-reported| Apr 2026       | 2026-05-12                  | BLS (CPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/cpi_05122026.htm#:~:text=shelter%20index%20also%20increased%20in,2%20percent))                                     | observed    |
| CPI_ENERGY_MOM            | CPI               | percent change (MoM)           | 3.8          | percent | not provided              | not source-reported| Apr 2026       | 2026-05-12                  | BLS (CPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/cpi_05122026.htm#:~:text=The%20index%20for%20energy%20rose,percent%20over%20the%20month%20as))                                     | observed    |
| PCE_HEADLINE_MOM            | PCE               | percent change (MoM)           | 0.4          | percent | 0.7                        | month-over-month   | Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/index.php/news/2026/personal-income-and-outlays-april-2026#:~:text=From%20the%20preceding%20month%2C%20the,2%20percent))                         | observed    |
| PCE_HEADLINE_YOY            | PCE               | percent change (YoY)           | 3.8          | percent | 3.5                        | year-over-year     | Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/index.php/news/2026/personal-income-and-outlays-april-2026#:~:text=From%20the%20preceding%20month%2C%20the,2%20percent))                         | observed    |
| PCE_CORE_MOM                | PCE               | percent change (MoM)           | 0.2          | percent | 0.3                        | month-over-month   | Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/index.php/news/2026/personal-income-and-outlays-april-2026#:~:text=From%20the%20preceding%20month%2C%20the,2%20percent))                         | observed    |
| PCE_CORE_YOY                | PCE               | percent change (YoY)           | 3.3          | percent | 3.2                        | year-over-year     | Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/index.php/news/2026/personal-income-and-outlays-april-2026#:~:text=From%20the%20same%20month%20one,percent%20from%20one%20year%20ago))                         | observed    |
| PCE_GOODS_MOM               | PCE               | percent change (MoM)           | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| PCE_SERVICES_MOM           | PCE               | percent change (MoM)           | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| PPI_FINAL_DEMAND_MOM        | PPI               | percent change (MoM)           | 1.4          | percent | 0.7                        | month-over-month   | Apr 2026       | 2026-05-13                  | BLS (PPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/ppi.htm#:~:text=The%20Producer%20Price%20Index%20for,month%20increase))                                  | observed    |
| PPI_FINAL_DEMAND_YOY        | PPI               | percent change (YoY)           | 6.0          | percent | not provided              | year-over-year     | Apr 2026       | 2026-05-13                  | BLS (PPI News Release, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/ppi.htm#:~:text=rising%201,4))                                  | observed    |
| UNEMPLOYMENT_RATE           | Labor             | rate                           | 4.3          | percent | 4.3                        | month-over-month   | May 2026       | 2026-06-05                  | BLS (Employment Situation, May 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/empsit_06052026.htm#:~:text=Total%20nonfarm%20payroll%20employment%20increased,Employment%20in%20financial%20activities%20declined))                             | observed    |
| U6_UNEMPLOYMENT_RATE        | Labor             | rate                           | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| LABOR_FORCE_PARTICIPATION_RATE | Labor          | rate                           | 61.8         | percent | 61.8                       | month-over-month   | May 2026       | 2026-06-05                  | BLS (Employment Situation, May 2026) ([www.bls.gov](https://www.bls.gov/news.release/empsit.nr0.htm#:~:text=The%20labor%20force%20participation%20rate,change%20over%20the%20year%2C%20after))                             | observed    |
| NONFARM_PAYROLLS            | Labor             | change (thousands)             | 172          | thousand| 179                        | month-over-month   | May 2026       | 2026-06-05                  | BLS (Employment Situation, May 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/empsit_06052026.htm#:~:text=Total%20nonfarm%20payroll%20employment%20increased,Employment%20in%20financial%20activities%20declined))                             | observed    |
| AVERAGE_HOURLY_EARNINGS_MOM  | Labor             | percent change (MoM)           | 0.3          | percent | 0.2                        | month-over-month   | May 2026       | 2026-06-05                  | BLS (Employment Situation, May 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/empsit_06052026.htm#:~:text=In%20May%2C%20average%20hourly%20earnings,hourly%20earnings%20have%20increased%20by))                              | observed    |
| AVERAGE_HOURLY_EARNINGS_YOY  | Labor             | percent change (YoY)           | 3.4          | percent | 3.6                        | year-over-year     | May 2026       | 2026-06-05                  | BLS (Employment Situation, May 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/empsit_06052026.htm#:~:text=In%20May%2C%20average%20hourly%20earnings,hourly%20earnings%20have%20increased%20by))                              | observed    |
| AVERAGE_WEEKLY_HOURS        | Labor             | level (hours)                  | 34.3         | hours   | 34.3                       | month-over-month   | May 2026       | 2026-06-05                  | BLS (Employment Situation, May 2026) ([www.bls.gov](https://www.bls.gov/news.release/archives/empsit_06052026.htm#:~:text=AVERAGE%20WEEKLY%20HOURS%20%20,45.6))                             | observed    |
| INITIAL_JOBLESS_CLAIMS      | Labor             | level                          | not provided | people  | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| CONTINUING_JOBLESS_CLAIMS   | Labor             | level                          | not provided | people  | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| JOLTS_JOB_OPENINGS          | Labor             | level (millions)               | 7.6          | million | 0.731                      | month-over-month   | Apr 2026       | 2026-06-02                  | BLS (JOLTS, Apr 2026) ([www.bls.gov](https://www.bls.gov/news.release/jolts.htm#:~:text=Job%20Openings))                                           | observed    |
| REAL_GDP_QOQ_SAAR           | GDP               | percent change (QoQ, annual)   | 1.6          | percent | 0.5                        | quarter-over-quarter | Q1 2026     | 2026-05-26                  | BEA (GDP second estimate, Q1 2026) ([www.bea.gov](https://www.bea.gov/data/gdp/gross-domestic-product#:~:text=GDP%20,Profits%2C%201st%20Quarter%202026))                                | observed    |
| GDP_PRICE_INDEX            | GDP               | percent change (QoQ, annual)   | 3.6          | percent | 3.7                        | quarter-over-quarter | Q1 2026     | 2026-04-30                  | BEA (GDP advance estimate, Q1 2026) ([www.bea.gov](https://www.bea.gov/news/2026/gdp-advance-estimate-1st-quarter-2026#:~:text=The%20price%20index%20for%20gross,9%20percent%2C%20and%20the))                            | observed    |
| RETAIL_SALES_MOM            | Retail            | percent change (MoM)           | 0.5          | percent | 1.6                        | month-over-month   | Apr 2026       | 2026-05-14                  | U.S. Census (Advance Retail Sales, Apr 2026) ([www.census.gov](https://www.census.gov/retail/sales.html#:~:text=Advance%20estimates%20of%20U,from%20March%202026%2C%20and%20up))                   | observed    |
| RETAIL_SALES_YOY            | Retail            | percent change (YoY)           | 4.9          | percent | not provided              | not source-reported| Apr 2026       | 2026-05-14                  | U.S. Census (Advance Retail Sales, Apr 2026) ([www.census.gov](https://www.census.gov/retail/sales.html#:~:text=Advance%20estimates%20of%20U,from%20March%202026%2C%20and%20up))                   | observed    |
| RETAIL_SALES_CONTROL_GROUP_MOM | Retail         | percent change (MoM)           | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| PERSONAL_INCOME_MOM         | Income            | percent change (MoM)           | -0.1         | percent | 0.6                        | month-over-month   | Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/data/income-saving/personal-income#:~:text=monthly%20rate,Personal))                         | observed    |
| PERSONAL_SPENDING_MOM       | Spending          | percent change (MoM)           | 0.5          | percent | 0.9                        | month-over-month   | Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/data/income-saving/personal-income#:~:text=monthly%20rate,Personal))                         | observed    |
| PERSONAL_SAVING_RATE        | Saving            | rate                           | 2.6          | percent | not provided              | not source-reported| Apr 2026       | 2026-05-28                  | BEA (Personal Income & Outlays, Apr 2026) ([www.bea.gov](https://www.bea.gov/data/income-saving/personal-income#:~:text=billion%20in%20April%2C%20and%20the,6%20percent))                         | observed    |
| CONSUMER_CREDIT             | Credit            | level                          | not provided | USD     | not provided              | not source-reported| latest available | not provided            | not provided                                                                  | not_provided|
| DURABLE_GOODS_ORDERS_MOM    | Manufacturing     | percent change (MoM)           | 7.9          | percent | 1.3                        | month-over-month   | Apr 2026       | 2026-05-28                  | Census (Durable Goods, Apr 2026) ([www.census.gov](https://www.census.gov/manufacturing/m3/adv/current/index.html#:~:text=New%20orders%20for%20manufactured%20durable,9%20billion))                               | observed    |
| FACTORY_ORDERS_MOM          | Manufacturing     | percent change (MoM)           | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| US_TRADE_BALANCE            | External Trade    | balance (USD)                  | not provided | USD     | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| INDUSTRIAL_PRODUCTION_MOM   | Industrial Prod.  | percent change (MoM)           | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| CAPACITY_UTILIZATION        | Industrial Prod.  | utilization rate               | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_MANUFACTURING_PMI       | Business Survey   | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_MANUFACTURING_NEW_ORDERS | Business Survey  | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_MANUFACTURING_PRICES    | Business Survey   | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_MANUFACTURING_EMPLOYMENT | Business Survey  | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_SERVICES_PMI           | Business Survey   | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_SERVICES_NEW_ORDERS    | Business Survey   | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_SERVICES_PRICES        | Business Survey   | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| ISM_SERVICES_EMPLOYMENT    | Business Survey   | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| CONSUMER_SENTIMENT         | Survey            | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| CONSUMER_INFLATION_EXPECTATIONS_1Y | Survey    | percentage                     | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| CONSUMER_INFLATION_EXPECTATIONS_5Y | Survey    | percentage                     | not provided | percent | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| CONSUMER_CONFIDENCE        | Survey            | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| HOUSING_STARTS            | Housing           | thousands of units             | not provided | units   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| BUILDING_PERMITS          | Housing           | thousands of units             | not provided | units   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| EXISTING_HOME_SALES       | Housing           | millions of units              | not provided | units   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| NEW_HOME_SALES            | Housing           | thousands of units             | not provided | units   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|
| PENDING_HOME_SALES        | Housing           | index                          | not provided | index   | not provided              | not provided       | not provided   | not provided               | not provided                                                                  | not_provided|

## 3. Rates Credit Liquidity Volatility Datapoints

| indicator_id                                   | data_area     | measure                              | latest_value | unit    | source_reported_comparison | comparison_type | period_covered/observed | release_or_observation_date | source                                | status      |
|-----------------------------------------------|---------------|--------------------------------------|--------------|---------|----------------------------|-----------------|------------------------|-----------------------------|----------------------------------------|-------------|
| FED_FUNDS_TARGET_RANGE                         | Monetary Policy | target range effectively applied      | 5.25–5.50    | percent | not provided              | not provided    | 2026-06-09 onward      | 2026-05-04                  | Federal Reserve (May 2026 FOMC statement) | observed    |
| LATEST_FOMC_DECISION                         | Monetary Policy | target range decision               | Hold at 5.25–5.50 | percent | not provided           | not provided    | May 2026 meeting       | 2026-05-04                  | Federal Reserve (May 3-4, 2026 statement) | observed    |
| NEXT_FOMC_MEETING                            | Monetary Policy | date of meeting                    | 2026-06-16–2026-06-17 | date  | not provided           | not provided    | scheduled              | not source-reported             | Federal Reserve (FOMC schedule)         | scheduled   |
| MARKET_IMPLIED_NEXT_FOMC_PROBABILITY         | Market Data    | probability                         | not provided | percent | not provided              | not provided    | N/A                    | N/A                         | not provided                          | not_provided|
| EFFECTIVE_FED_FUNDS_RATE                     | Monetary Policy | effective rate                      | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| SOFR                                         | Rates          | Secured Overnight Financing Rate     | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_3M                                  | Rates          | 3-month Treasury yield             | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_2Y                                  | Rates          | 2-year Treasury yield             | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_5Y                                  | Rates          | 5-year Treasury yield             | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_10Y                                 | Rates          | 10-year Treasury yield            | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_30Y                                 | Rates          | 30-year Treasury yield            | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| REAL_YIELD_5Y                                | Rates          | 5-year Treasury Inflation-Protected yield | not provided | percent | not provided | not provided | latest available | N/A           | not provided                          | not_provided|
| REAL_YIELD_10Y                               | Rates          | 10-year TIPS yield               | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| BREAKEVEN_INFLATION_5Y                       | Market Data    | 5-year inflation breakeven         | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| BREAKEVEN_INFLATION_10Y                      | Market Data    | 10-year inflation breakeven        | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| INFLATION_SWAP_OR_MARKET_EXPECTATION_1Y      | Market Data    | 1-year inflation swap rate        | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_10Y_2Y_SPREAD                       | Rates          | 10y–2y Treasury yield spread      | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_10Y_3M_SPREAD                       | Rates          | 10y–3m Treasury yield spread     | not provided | percent | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| US_DOLLAR_INDEX                              | Currencies     | DXY Index level                   | not provided | index   | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| VIX                                          | Volatility     | CBOE VIX index                   | not provided | index   | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| MOVE_INDEX                                   | Volatility     | ICE BofA MOVE index              | not provided | index   | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| INVESTMENT_GRADE_OAS                         | Credit         | ICE BofA US Corp A or better OAS | not provided | basis points | not provided           | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| HIGH_YIELD_OAS                              | Credit         | ICE BofA US High Yield OAS       | not provided | basis points | not provided           | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| FINANCIAL_CONDITIONS_INDEX                   | Conditions     | index                           | not provided | index   | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| MONEY_MARKET_FUND_ASSETS                    | Liquidity      | total assets (USD)              | not provided | USD     | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| FED_BALANCE_SHEET_TOTAL_ASSETS              | Fed            | total assets (USD)              | not provided | USD     | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| RESERVE_BALANCES_WITH_FEDERAL_RESERVE        | Fed            | reserves (USD)                  | not provided | USD     | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| TREASURY_GENERAL_ACCOUNT                    | Treasury       | TGA balance (USD)               | not provided | USD     | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| REVERSE_REPO                                | Fed            | reverse repo (USD)             | not provided | USD     | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| M2_MONEY_STOCK                              | Fed            | M2 money supply                | not provided | USD     | not provided              | not provided    | latest available       | N/A                         | not provided                          | not_provided|
| MORTGAGE_30Y_FIXED_RATE                     | Rates          | 30-year mortgage rate (Freddie Mac) | not provided | percent | not provided         | not provided    | latest available       | N/A                         | not provided                          | not_provided|

## 4. Commodity And Currency Datapoints

| indicator_id               | measure        | latest_value | unit    | source_reported_comparison | comparison_type | observation_date | source       | status      |
|----------------------------|----------------|--------------|---------|----------------------------|-----------------|------------------|--------------|-------------|
| WTI_CRUDE                  | price          | not provided | USD/bbl | not provided              | not provided    | not provided     | not provided | not_provided|
| BRENT_CRUDE                | price          | not provided | USD/bbl | not provided              | not provided    | not provided     | not provided | not_provided|
| NATURAL_GAS                | price          | not provided | USD/MMBtu | not provided             | not provided    | not provided     | not provided | not_provided|
| GOLD                       | price          | not provided | USD/oz | not provided               | not provided    | not provided     | not provided | not_provided|
| SILVER                     | price          | not provided | USD/oz | not provided               | not provided    | not provided     | not provided | not_provided|
| COPPER                     | price          | not provided | USD/lb | not provided               | not provided    | not provided     | not provided | not_provided|
| BROAD_COMMODITY_INDEX     | index          | not provided | index  | not provided               | not provided    | not provided     | not provided | not_provided|
| US_DOLLAR_INDEX           | index          | not provided | index  | not provided               | not provided    | not provided     | not provided | not_provided|
| EURUSD                     | exchange rate  | not provided |         | not provided               | not provided    | not provided     | not provided | not_provided|
| USDJPY                     | exchange rate  | not provided |         | not provided               | not provided    | not provided     | not provided | not_provided|
| BITCOIN                    | price (USD)    | not provided | USD    | not provided               | not provided    | not provided     | not provided | not_provided|
| ETHEREUM                   | price (USD)    | not provided | USD    | not provided               | not provided    | not provided     | not provided | not_provided|

## 5. Broad Equity Market Datapoints

| indicator_id                            | data_area        | measure                    | latest_value | unit | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source      | status      |
|-----------------------------------------|------------------|------------------------|--------------|------|----------------------------|-----------------|----------------|-----------------------------|-------------|-------------|
| SP500_INDEX_LEVEL                       | Equity           | index level             | not provided | index| not provided              | not provided    | not provided   | not provided               | not provided | not_provided|
| NASDAQ_COMPOSITE_INDEX_LEVEL            | Equity           | index level             | not provided | index| not provided              | not provided    | not provided   | not provided               | not provided | not_provided|
| RUSSELL_2000_INDEX_LEVEL                | Equity           | index level             | not provided | index| not provided              | not provided    | not provided   | not provided               | not provided | not_provided|
| SP500_FORWARD_PE_OR_CAPE                | Valuation        | forward P/E or CAPE     | not provided | ratio| not provided             | not provided    | not provided   | not provided               | not provided | not_provided|
| SP500_EARNINGS_GROWTH_ESTIMATE          | Earnings         | forecast growth         | not provided | percent| not provided            | not provided    | not provided   | not provided               | not provided | not_provided|
| SP500_EARNINGS_REVISION_OR_BEAT_RATE    | Earnings         | revision or beat rate   | not provided | percent| not provided            | not provided    | not provided   | not provided               | not provided | not_provided|
| US_EQUITY_MARKET_BREADTH                | Breadth          | index or ratio          | not provided | index| not provided              | not provided    | not provided   | not provided               | not provided | not_provided|
| EQUAL_WEIGHT_VS_CAP_WEIGHT_CONTEXT      | Breadth          | comparison index        | not provided | index| not provided             | not provided    | not provided   | not provided               | not provided | not_provided|
| EQUITY_PUT_CALL_RATIO                   | Market          | ratio                   | not provided | ratio| not provided              | not provided    | not provided   | not provided               | not provided | not_provided|
| INVESTOR_SENTIMENT_SURVEY              | Sentiment        | index                   | not provided | index| not provided             | not provided    | not provided   | not provided               | not provided | not_provided|
| US_EQUITY_FUND_FLOWS                    | Flows            | net flows (USD)         | not provided | USD  | not provided             | not provided    | not provided   | not provided               | not provided | not_provided|
| ETF_FUND_FLOWS_EQUITY_BOND_CASH         | Flows            | net flows (USD)         | not provided | USD  | not provided             | not provided    | not provided   | not provided               | not provided | not_provided|
| MARGIN_DEBT_OR_LEVERAGE_DATAPOINT       | Leverage         | index or level          | not provided | index| not provided              | not provided    | not provided   | not provided               | not provided | not_provided|
| IMPLIED_CORRELATION_OR_REALIZED_CORRELATION | Correlation  | index or measure        | not provided | index| not provided             | not provided    | not provided   | not provided               | not provided | not_provided|

## 6. Scheduled Macro Events

| event_id | date | event | publisher_or_entity | release_type | consensus_or_forecast_if_source_reported | source | status |
|---|---|---|---|---|---|---|---|
| NEXT_CPI_RELEASE | June 10, 2026 8:30 AM ET | CPI, May 2026 | U.S. Bureau of Labor Statistics | inflation release | not source-reported | BLS Release Calendar - https://www.bls.gov/schedule/news_release/cpi.htm | scheduled |
| NEXT_PCE_RELEASE | outside scoring window | Personal Income and Outlays, May 2026 | U.S. Bureau of Economic Analysis | inflation and income release | not source-reported | BEA Release Schedule - https://www.bea.gov/news/schedule | outside_window |
| NEXT_PPI_RELEASE | June 11, 2026 8:30 AM ET | Producer Price Index, May 2026 | U.S. Bureau of Labor Statistics | inflation release | not source-reported | BLS Release Calendar - https://www.bls.gov/schedule/news_release/ppi.htm | scheduled |
| NEXT_EMPLOYMENT_REPORT | outside scoring window | Employment Situation, June 2026 | U.S. Bureau of Labor Statistics | labor market release | not source-reported | BLS Schedule of Releases - https://www.bls.gov/schedule/2026/home.htm | outside_window |
| NEXT_RETAIL_SALES_RELEASE | outside scoring window | Advance Monthly Sales for Retail and Food Services, May 2026 | U.S. Census Bureau | economic data release | not source-reported | U.S. Census Monthly Retail Trade - https://www.census.gov/retail/sales.html | outside_window |
| NEXT_GDP_RELEASE | outside scoring window | Q1 2026 GDP third estimate | U.S. Bureau of Economic Analysis | economic data release | not source-reported | BEA Release Schedule - https://www.bea.gov/news/schedule | outside_window |
| NEXT_ISM_MANUFACTURING_RELEASE | outside scoring window | ISM Manufacturing PMI, June 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar - https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/ | outside_window |
| NEXT_ISM_SERVICES_RELEASE | outside scoring window | ISM Services PMI, June 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar - https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/ | outside_window |
| NEXT_FOMC_DECISION | outside scoring window | FOMC meeting | Federal Reserve | monetary policy decision | not source-reported | Federal Reserve FOMC Calendar - https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | outside_window |
| NEXT_FOMC_MINUTES | outside scoring window | FOMC minutes | Federal Reserve | monetary policy minutes | not source-reported | Federal Reserve FOMC Calendar - https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | outside_window |
| NEXT_TREASURY_REFUNDING_OR_MAJOR_AUCTION | June 10-11, 2026 | 10-year Treasury note and 30-year Treasury bond auctions | U.S. Treasury | Treasury auctions | not source-reported | U.S. Treasury Tentative Auction Schedule - https://home.treasury.gov/system/files/221/Tentative-Auction-Schedule.pdf | scheduled |
| NEXT_ECB_DECISION | June 11, 2026 | Governing Council monetary policy decision | European Central Bank | monetary policy decision | not source-reported | ECB Governing Council Calendar - https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html | scheduled |
| NEXT_BOJ_DECISION | outside scoring window | Monetary Policy Meeting | Bank of Japan | monetary policy decision | not source-reported | Bank of Japan MPM Schedule - https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm | outside_window |
| NEXT_BOE_DECISION | outside scoring window | Monetary Policy Committee decision | Bank of England | monetary policy decision | not source-reported | Bank of England Monetary Policy Committee dates - https://www.bankofengland.co.uk/monetary-policy/upcoming-mpc-dates | outside_window |
| NEXT_PBOC_LPR_FIXING | outside scoring window | Loan Prime Rate fixing | People's Bank of China and National Interbank Funding Center | policy-rate fixing | not source-reported | National Interbank Funding Center LPR - https://www.chinamoney.com.cn/english/bmklpr/ | outside_window |
| NEXT_JOBLESS_CLAIMS_RELEASE | June 11, 2026 | Unemployment Insurance Weekly Claims | U.S. Department of Labor | labor market release | not source-reported | U.S. Department of Labor UI Claims - https://www.dol.gov/ui/data.pdf | scheduled |
| NEXT_JOLTS_RELEASE | outside scoring window | Job Openings and Labor Turnover Survey, May 2026 | U.S. Bureau of Labor Statistics | labor market release | not source-reported | BLS JOLTS - https://www.bls.gov/news.release/jolts.nr0.htm | outside_window |
| NEXT_DURABLE_GOODS_RELEASE | outside scoring window | Durable Goods Manufacturers' Shipments, Inventories, and Orders, May 2026 advance | U.S. Census Bureau | manufacturing release | not source-reported | Census Advance Report on Durable Goods - https://www.census.gov/manufacturing/m3/adv/current/index.html | outside_window |
| NEXT_TRADE_BALANCE_RELEASE | outside scoring window | U.S. International Trade in Goods and Services, May 2026 | U.S. Census Bureau and Bureau of Economic Analysis | trade release | not source-reported | BEA Release Schedule - https://www.bea.gov/news/schedule | outside_window |
| NEXT_INDUSTRIAL_PRODUCTION_RELEASE | outside scoring window | Industrial Production and Capacity Utilization, May 2026 | Federal Reserve | production release | not source-reported | Federal Reserve Statistical Release Calendar - https://www.federalreserve.gov/data/releaseschedule.htm | outside_window |
| NEXT_CONSUMER_SENTIMENT_RELEASE | June 12, 2026 10:00 AM ET | University of Michigan Consumer Sentiment, June 2026 preliminary | University of Michigan Surveys of Consumers | consumer survey release | not source-reported | University of Michigan Surveys of Consumers - https://www.sca.isr.umich.edu/ | scheduled |
| NEXT_CONSUMER_CONFIDENCE_RELEASE | outside scoring window | Consumer Confidence Index, June 2026 | The Conference Board | consumer survey release | not source-reported | The Conference Board Consumer Confidence - https://www.conference-board.org/topics/consumer-confidence | outside_window |
| NEXT_HOUSING_STARTS_RELEASE | outside scoring window | New Residential Construction, May 2026 | U.S. Census Bureau and HUD | housing release | not source-reported | Census/HUD New Residential Construction - https://www.census.gov/construction/nrc/ | outside_window |
| NEXT_EXISTING_HOME_SALES_RELEASE | outside scoring window | Existing-Home Sales, May 2026 | National Association of Realtors | housing release | not source-reported | NAR Existing-Home Sales - https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales | outside_window |
| NEXT_NEW_HOME_SALES_RELEASE | outside scoring window | New Residential Sales, May 2026 | U.S. Census Bureau and HUD | housing release | not source-reported | Census New Residential Sales - https://www.census.gov/construction/nrs/ | outside_window |
| NEXT_MAJOR_INDEX_EARNINGS_UPDATE | not provided | major index earnings update | not provided | earnings update | not provided | not provided | not_provided |

## 7. Missing Macro Datapoints

| section | indicator_or_event_id | missing_item | note |
|---|---|---|---|
| 2. Core Macro Datapoints   | PCE_GOODS_MOM | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | PCE_SERVICES_MOM | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | U6_UNEMPLOYMENT_RATE | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | INITIAL_JOBLESS_CLAIMS | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CONTINUING_JOBLESS_CLAIMS | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | RETAIL_SALES_CONTROL_GROUP_MOM | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CONSUMER_CREDIT | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | FACTORY_ORDERS_MOM | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | US_TRADE_BALANCE | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | INDUSTRIAL_PRODUCTION_MOM | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CAPACITY_UTILIZATION | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_MANUFACTURING_PMI | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_MANUFACTURING_NEW_ORDERS | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_MANUFACTURING_PRICES | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_MANUFACTURING_EMPLOYMENT | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_SERVICES_PMI | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_SERVICES_NEW_ORDERS | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_SERVICES_PRICES | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | ISM_SERVICES_EMPLOYMENT | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CONSUMER_SENTIMENT | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CONSUMER_INFLATION_EXPECTATIONS_1Y | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CONSUMER_INFLATION_EXPECTATIONS_5Y | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | CONSUMER_CONFIDENCE | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | HOUSING_STARTS | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | BUILDING_PERMITS | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | EXISTING_HOME_SALES | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | NEW_HOME_SALES | latest requested datapoint | not provided in source reports |
| 2. Core Macro Datapoints   | PENDING_HOME_SALES | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | MARKET_IMPLIED_NEXT_FOMC_PROBABILITY | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | EFFECTIVE_FED_FUNDS_RATE | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | SOFR | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_3M | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_2Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_5Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_10Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_30Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | REAL_YIELD_5Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | REAL_YIELD_10Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | BREAKEVEN_INFLATION_5Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | BREAKEVEN_INFLATION_10Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | INFLATION_SWAP_OR_MARKET_EXPECTATION_1Y | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_10Y_2Y_SPREAD | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_10Y_3M_SPREAD | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | US_DOLLAR_INDEX | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | VIX | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | MOVE_INDEX | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | INVESTMENT_GRADE_OAS | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | HIGH_YIELD_OAS | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | FINANCIAL_CONDITIONS_INDEX | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | MONEY_MARKET_FUND_ASSETS | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | FED_BALANCE_SHEET_TOTAL_ASSETS | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | RESERVE_BALANCES_WITH_FEDERAL_RESERVE | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | TREASURY_GENERAL_ACCOUNT | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | REVERSE_REPO | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | M2_MONEY_STOCK | latest requested datapoint | not provided in source reports |
| 3. Rates Credit Liquidity Volatility Datapoints   | MORTGAGE_30Y_FIXED_RATE | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | WTI_CRUDE | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | BRENT_CRUDE | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | NATURAL_GAS | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | GOLD | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | SILVER | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | COPPER | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | BROAD_COMMODITY_INDEX | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | US_DOLLAR_INDEX | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | EURUSD | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | USDJPY | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | BITCOIN | latest requested datapoint | not provided in source reports |
| 4. Commodity And Currency Datapoints   | ETHEREUM | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | SP500_INDEX_LEVEL | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | NASDAQ_COMPOSITE_INDEX_LEVEL | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | RUSSELL_2000_INDEX_LEVEL | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | SP500_FORWARD_PE_OR_CAPE | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | SP500_EARNINGS_GROWTH_ESTIMATE | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | SP500_EARNINGS_REVISION_OR_BEAT_RATE | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | US_EQUITY_MARKET_BREADTH | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | EQUAL_WEIGHT_VS_CAP_WEIGHT_CONTEXT | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | EQUITY_PUT_CALL_RATIO | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | INVESTOR_SENTIMENT_SURVEY | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | US_EQUITY_FUND_FLOWS | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | ETF_FUND_FLOWS_EQUITY_BOND_CASH | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | MARGIN_DEBT_OR_LEVERAGE_DATAPOINT | latest requested datapoint | not provided in source reports |
| 5. Broad Equity Market Datapoints   | IMPLIED_CORRELATION_OR_REALIZED_CORRELATION | latest requested datapoint | not provided in source reports |
| Section 6 | NEXT_PCE_RELEASE | Personal Income and Outlays, May 2026 | outside_window |
| Section 6 | NEXT_EMPLOYMENT_REPORT | Employment Situation, June 2026 | outside_window |
| Section 6 | NEXT_RETAIL_SALES_RELEASE | Advance Monthly Sales for Retail and Food Services, May 2026 | outside_window |
| Section 6 | NEXT_GDP_RELEASE | Q1 2026 GDP third estimate | outside_window |
| Section 6 | NEXT_ISM_MANUFACTURING_RELEASE | ISM Manufacturing PMI, June 2026 | outside_window |
| Section 6 | NEXT_ISM_SERVICES_RELEASE | ISM Services PMI, June 2026 | outside_window |
| Section 6 | NEXT_FOMC_DECISION | FOMC meeting | outside_window |
| Section 6 | NEXT_FOMC_MINUTES | FOMC minutes | outside_window |
| Section 6 | NEXT_BOJ_DECISION | Monetary Policy Meeting | outside_window |
| Section 6 | NEXT_BOE_DECISION | Monetary Policy Committee decision | outside_window |
| Section 6 | NEXT_PBOC_LPR_FIXING | Loan Prime Rate fixing | outside_window |
| Section 6 | NEXT_JOLTS_RELEASE | Job Openings and Labor Turnover Survey, May 2026 | outside_window |
| Section 6 | NEXT_DURABLE_GOODS_RELEASE | Durable Goods Manufacturers' Shipments, Inventories, and Orders, May 2026 advance | outside_window |
| Section 6 | NEXT_TRADE_BALANCE_RELEASE | U.S. International Trade in Goods and Services, May 2026 | outside_window |
| Section 6 | NEXT_INDUSTRIAL_PRODUCTION_RELEASE | Industrial Production and Capacity Utilization, May 2026 | outside_window |
| Section 6 | NEXT_CONSUMER_CONFIDENCE_RELEASE | Consumer Confidence Index, June 2026 | outside_window |
| Section 6 | NEXT_HOUSING_STARTS_RELEASE | New Residential Construction, May 2026 | outside_window |
| Section 6 | NEXT_EXISTING_HOME_SALES_RELEASE | Existing-Home Sales, May 2026 | outside_window |
| Section 6 | NEXT_NEW_HOME_SALES_RELEASE | New Residential Sales, May 2026 | outside_window |
| Section 6 | NEXT_MAJOR_INDEX_EARNINGS_UPDATE | major index earnings update | not_provided |
