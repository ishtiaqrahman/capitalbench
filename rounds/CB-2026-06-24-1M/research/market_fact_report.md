# Prompt 1 - Market Fact Report

Research cutoff: 2026-06-24T21:20:00Z

Rounds prepared from this report:

| round | horizon | entry date | exit date | decision deadline |
| --- | --- | --- | --- | --- |
| CB-2026-06-24-1W | one week | 2026-06-24 | 2026-07-01 | 2026-06-25T02:30:00Z |
| CB-2026-06-24-1M | one month | 2026-06-24 | 2026-07-24 | 2026-06-25T02:30:00Z |

## Source Ledger

Narrative facts were gathered manually from public web pages and official releases. No model API was used to generate these research artifacts. CapitalBench generated the June 24 full-universe price, risk, and benchmark-relative artifacts from market-data fetches before this report was finalized. The entry-price files were derived from the same frozen `as_of_adj_close` values in those full-universe artifacts after the direct full-universe entry-price fetch returned HTTP 429.

| source | URL | facts used |
| --- | --- | --- |
| AP News, June 24 index close | https://apnews.com/article/wall-street-dow-nasdaq-24ec698bae58c75ad6ca4536196502ae | major U.S. index closes, daily changes, week-to-date changes, and year-to-date changes |
| AP News, June 24 market narrative | https://apnews.com/article/stocks-markets-ai-us-iran-oil-b631564d3b359644eda586b047c9bcf0 | technology-weighted market pressure, breadth context, oil, gold, Treasury yield, and company-level moves |
| Federal Reserve FOMC statement, June 17 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm | target range and policy statement facts |
| Federal Reserve H.15 current release | https://www.federalreserve.gov/releases/h15/ | June 24 release and June 23 rate observations |
| BLS CPI May release | https://www.bls.gov/news.release/cpi.nr0.htm | May CPI datapoints |
| Census retail sales | https://www.census.gov/retail/sales.html | May 2026 advance retail sales |
| Census and HUD new residential sales | https://www.census.gov/construction/nrs/current/index.html | May 2026 new-home sales, inventory, supply, and prices |
| BEA international transactions release | https://www.bea.gov/news/2026/us-international-transactions-and-investment-position-1st-quarter-2026-and-annual-update | Q1 current-account and net international investment position facts |
| BEA release schedule | https://www.bea.gov/news/schedule | June 25, July 7, July 24, and July 30 scheduled releases |
| EIA weekly petroleum status report | https://ir.eia.gov/wpsr/wpsrsummary.pdf | week-ending June 19 petroleum inventory and supply facts |
| S&P Global Flash US PMI | https://www.pmi.spglobal.com/Public/Home/PressRelease/0f8762edff954b619d90d12531497919 | June flash PMI values and survey dates |
| Micron investor release | https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-record-results-third-quarter | fiscal Q3 2026 revenue, income, margin, guidance, and product facts |
| Kiplinger economic calendar | https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar | June 25 PCE/GDP/durable-goods/jobless-claims schedule and PCE forecast values attributed to Wells Fargo |
| Generated CapitalBench market data | rounds/CB-2026-06-24-1W/market_data/universe_trailing_returns.csv | complete 70-option mechanical price, risk, and benchmark-relative context |
| Generated CapitalBench entry prices | rounds/CB-2026-06-24-1W/prices/entry_prices.csv | June 24 official entry prices derived from the frozen full-universe table |

## Market Close Snapshot

AP reported a mixed Wednesday, June 24 U.S. close. The S&P 500 fell 0.1%, the Nasdaq Composite fell 0.4%, the Dow Jones Industrial Average rose 0.4%, and the Russell 2000 rose 0.4%.

| index | June 24 close | daily change | week-to-date change | year-to-date change |
| --- | ---: | ---: | ---: | ---: |
| S&P 500 | 7,358.22 | -7.24 / -0.1% | -1.9% | +7.5% |
| Dow Jones Industrial Average | 51,848.90 | +182.06 / +0.4% | +0.6% | +7.9% |
| Nasdaq Composite | 25,476.64 | -110.40 / -0.4% | -3.9% | +9.6% |
| Russell 2000 | 2,986.63 | +11.15 / +0.4% | +0.2% | +20.3% |

AP said more stocks rose than fell within the S&P 500, while several large technology weights pulled down the capitalization-weighted index. AP reported Microsoft down 2.3%, Oracle down 4.6%, Exxon Mobil down 2.0%, Chevron down 2.6%, KB Home up 16.7%, and D.R. Horton up 6.7%.

## Monetary Policy, Rates, Inflation, And Consumption

The FOMC maintained the federal funds target range at 3.50%-3.75% on June 17, 2026. The statement said economic activity was expanding at a solid pace, job gains had kept pace with the workforce, unemployment had changed little, and inflation remained elevated relative to the 2% goal.

Federal Reserve H.15 was released June 24, 2026. Selected June 23 observations:

| rate | value | observation date |
| --- | ---: | --- |
| effective federal funds rate | 3.63% | 2026-06-23 |
| 3-month Treasury bill, secondary market | 3.70% | 2026-06-23 |
| 2-year Treasury constant maturity | 4.16% | 2026-06-23 |
| 5-year Treasury constant maturity | 4.27% | 2026-06-23 |
| 10-year Treasury constant maturity | 4.50% | 2026-06-23 |
| 30-year Treasury constant maturity | 4.94% | 2026-06-23 |
| 5-year TIPS real yield | 2.03% | 2026-06-23 |
| 10-year TIPS real yield | 2.29% | 2026-06-23 |

AP reported that the 10-year Treasury yield fell to 4.40% on June 24 from 4.50% late Tuesday, and the 2-year Treasury yield eased to 4.15% from 4.16%.

May CPI increased 0.5% month over month and 4.2% year over year. Core CPI increased 0.2% month over month and 2.9% year over year. Energy increased 3.9% month over month and 23.5% year over year; gasoline increased 7.0% month over month and 40.5% year over year; shelter increased 0.3% month over month and 3.4% year over year.

May advance retail and food services sales were $763.7 billion, up 0.9% month over month and 6.9% year over year. Retail trade sales were up 1.0% month over month and 7.5% year over year. Nonstore retailers were up 12.2% year over year, and food services and drinking places were up 2.7% year over year.

## Growth, Housing, External Balance, And Survey Data

BEA's second estimate for Q1 real GDP showed 1.6% annualized growth. Real final sales to private domestic purchasers increased 2.4%; the gross domestic purchases price index increased 3.5%; the PCE price index increased 4.5%; core PCE increased 4.4%; real GDI increased 0.9%; and profits from current production increased $40.4 billion.

BEA reported that the Q1 current-account deficit widened by $5.8 billion, or 2.6%, to $226.8 billion. The deficit was 2.9% of current-dollar GDP. The U.S. net international investment position was -$21.27 trillion at the end of Q1, compared with a revised -$21.87 trillion at the end of Q4 2025.

Census and HUD reported May new single-family home sales at a seasonally adjusted annual rate of 580,000, down 7.3% from April and down 6.8% from May 2025. New houses for sale were 496,000, representing 10.3 months of supply. The median sales price was $424,900, up 2.0% from April and virtually unchanged from May 2025.

S&P Global's June flash U.S. PMI showed a composite PMI of 52.2, services PMI of 51.3, manufacturing output index of 57.7, and manufacturing PMI of 55.7. The release said data were collected from June 11 through June 22, 2026, and noted faster business activity growth, lower employment, and elevated price inflation.

## Energy, Commodities, And Technology Company Facts

AP reported Brent crude down 3.8% to $73.87 per barrel on June 24 and U.S. crude down 3.9% to $70.34. AP also reported gold down 3.4% to $4,008.80 per ounce.

EIA's weekly petroleum summary for the week ending June 19 reported commercial crude oil inventories down 6.1 million barrels to 412.1 million barrels, about 7% below the five-year average. Gasoline inventories increased 2.1 million barrels and were 5% below the five-year average; distillate inventories increased 3.1 million barrels and were about 10% below the five-year average. Refinery utilization was 96.1%.

Micron released fiscal Q3 2026 results at 4:01 p.m. EDT on June 24. Revenue was $41.46 billion, compared with $23.86 billion in the prior quarter and $9.30 billion a year earlier. GAAP net income was $28.24 billion, non-GAAP net income was $28.86 billion, GAAP gross margin was 84.6%, and non-GAAP gross margin was 84.9%. Micron guided fiscal Q4 revenue to $50.0 billion plus or minus $1.0 billion, gross margin to about 86%, and non-GAAP diluted EPS to $31.00 plus or minus $1.00. Product facts in the release included HBM4 high-volume shipments for the lead customer's platform and HBM4E volume production expected in calendar 2027.

## Generated Mechanical Price Context

CapitalBench generated a complete 70-option full-universe price, risk, and benchmark-relative context file for June 24 with no failed options. The generated artifact is stored at `rounds/CB-2026-06-24-1W/market_data/universe_trailing_returns.csv` and copied unchanged to the monthly round. It is sorted by option order, not by performance. The model-facing prompt builder appends the corresponding markdown artifact after the final briefing.

The direct full-universe entry-price command returned HTTP 429. Both rounds' `prices/entry_prices.csv` files were generated from the frozen `as_of_adj_close` values in the full-universe context file and labeled `universe_trailing_returns_adjclose` for non-cash options.

## In-Window Scheduled Dates

| date | event |
| --- | --- |
| 2026-06-25 | BEA GDP third estimate, industries, corporate profits, state GDP, and state personal income, Q1 2026 |
| 2026-06-25 | BEA Personal Income and Outlays, May 2026 |
| 2026-06-25 | Weekly jobless claims, durable goods, and related U.S. economic releases listed in public calendars |
| 2026-07-01 | Weekly round exit close |
| 2026-07-03 | Independence Day observed; Nasdaq and NYSE closed |
| 2026-07-07 | BEA U.S. International Trade in Goods and Services, May 2026 |
| 2026-07-24 | Monthly round exit close |
| 2026-07-30 | BEA GDP advance estimate for Q2 2026 and Personal Income and Outlays, June 2026 |
