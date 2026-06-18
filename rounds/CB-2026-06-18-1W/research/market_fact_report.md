# Prompt 1 - Market Fact Report

Research cutoff: 2026-06-18T22:05:22Z

Rounds prepared from this report:

| round | horizon | entry date | exit date | decision deadline |
| --- | --- | --- | --- | --- |
| CB-2026-06-18-1W | one week | 2026-06-18 | 2026-06-25 | 2026-06-19T02:30:00Z |
| CB-2026-06-18-1M | one month | 2026-06-18 | 2026-07-20 | 2026-06-19T02:30:00Z |

## Source Ledger

Narrative facts were gathered manually from public web pages and official releases. CapitalBench tooling generated official entry prices and trailing-return tables from configured market-data feeds after the close.

| source | URL | facts used |
| --- | --- | --- |
| AP News, June 18 market close | https://apnews.com/article/wall-street-stocks-dow-nasdaq-411ec68891aa5dc7d7f684e0305e2aa3 | major U.S. index closes, weekly changes, Juneteenth closure note |
| Federal Reserve FOMC statement, June 17 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm | target range, statement language on activity, labor, inflation |
| Federal Reserve June 17 SEP accessible table | https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm | 2026 median projections and dot distribution |
| Federal Reserve H.15 current release | https://www.federalreserve.gov/releases/h15/ | effective fed funds, Treasury bill, nominal Treasury, TIPS real yields through 2026-06-17 |
| Department of Labor UI claims, June 18 PDF | https://www.dol.gov/ui/data.pdf | initial claims, insured unemployment, moving averages |
| Philadelphia Fed MBOS June 2026 | https://www.philadelphiafed.org/surveys-and-data/regional-economic-analysis/mbos-2026-06 | regional manufacturing indexes and special questions |
| Census retail sales | https://www.census.gov/retail/sales.html | May 2026 advance retail sales |
| Census retail release schedule | https://www.census.gov/retail/release_schedule.html | July 16 release date for June 2026 advance retail trade |
| BLS CPI May release | https://www.bls.gov/news.release/cpi.nr0.htm | May CPI datapoints and next release date |
| BLS CPI release schedule | https://www.bls.gov/schedule/news_release/cpi.htm | July 14 release date for June CPI |
| BLS PPI May release | https://www.bls.gov/news.release/ppi.nr0.htm | May PPI datapoints |
| BLS PPI release schedule | https://www.bls.gov/schedule/news_release/ppi.htm | July 15 release date for June PPI |
| BLS Employment Situation May release | https://www.bls.gov/news.release/empsit.nr0.htm | May payroll, unemployment, participation, wages |
| BLS Employment Situation schedule | https://www.bls.gov/schedule/news_release/empsit.htm | July 2 release date for June employment |
| BEA Personal Income and Outlays, April | https://www.bea.gov/news/2026/personal-income-and-outlays-april-2026 | April PCE, personal income, spending, next release date |
| BEA release schedule | https://www.bea.gov/news/schedule | June 25 release date for May Personal Income and Outlays |
| Federal Reserve G.17 industrial production | https://www.federalreserve.gov/releases/g17/current/default.htm | May industrial production and capacity utilization |
| Census new residential construction | https://www.census.gov/construction/nrc/current/index.html | May housing starts, permits, completions |
| Nasdaq market holiday schedule | https://www.nasdaq.com/market-activity/stock-market-holiday-schedule | Juneteenth and July 3 market closures |
| Federal Reserve FOMC calendar | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | July 28-29 FOMC meeting date |
| Generated CapitalBench market data | rounds/CB-2026-06-18-1W/market_data/universe_trailing_returns.csv | selected mechanical return context |
| Generated CapitalBench entry prices | rounds/CB-2026-06-18-1W/prices/entry_prices.csv | June 18 official entry prices |

## Market Close Snapshot

The June 18 close replaced a stale working note that had carried June 17 down-market levels. The AP June 18 close showed a rebound:

| index | June 18 close | daily change | weekly change |
| --- | ---: | ---: | ---: |
| S&P 500 | 7,500.58 | +80.48 / +1.1% | +69.12 / +0.9% |
| Dow Jones Industrial Average | 51,564.70 | +72.15 / +0.1% | +362.44 / +0.7% |
| Nasdaq Composite | 26,517.93 | +496.28 / +1.9% | +629.09 / +2.4% |
| Russell 2000 | 2,979.77 | +61.78 / +2.1% | +35.77 / +1.2% |

AP also reported that crude prices wavered after the United States and Iran signed an agreement to end their war and reopen the Strait of Hormuz, Treasury yields eased, and U.S. markets would be closed Friday, June 19, 2026 for Juneteenth.

## Monetary Policy And Rates

The FOMC held the federal funds target range at 3.50%-3.75% on June 17, 2026 by a 12-0 vote. The statement said activity was expanding at a solid pace, job gains had kept pace with the workforce, unemployment had changed little, and inflation remained elevated relative to the 2% goal.

The June SEP median projections for 2026 were:

| projection | 2026 median |
| --- | ---: |
| real GDP growth | 2.2% |
| unemployment rate | 4.3% |
| PCE inflation | 3.6% |
| core PCE inflation | 3.3% |
| federal funds midpoint | 3.8% |

The 2026 dot distribution around the current 3.625 midpoint was: 9 participants above 3.625, 8 at 3.625, and 1 below 3.625.

Federal Reserve H.15, last released June 18 with observations through June 17, showed:

| rate | value | observation date |
| --- | ---: | --- |
| effective federal funds rate | 3.63% | 2026-06-17 |
| 3-month Treasury bill, secondary market | 3.68% | 2026-06-17 |
| 2-year Treasury constant maturity | 4.20% | 2026-06-17 |
| 5-year Treasury constant maturity | 4.27% | 2026-06-17 |
| 10-year Treasury constant maturity | 4.49% | 2026-06-17 |
| 30-year Treasury constant maturity | 4.93% | 2026-06-17 |
| 5-year TIPS real yield | 1.96% | 2026-06-17 |
| 10-year TIPS real yield | 2.23% | 2026-06-17 |

## Labor, Inflation, Consumption, And Production

The Department of Labor reported initial jobless claims of 226,000 for the week ended June 13, down 4,000 from the prior revised level of 230,000. The 4-week moving average was 223,250, up 4,000. Insured unemployment for the week ended June 6 was 1,810,000, up 24,000, and the insured unemployment rate was 1.2%.

May payrolls increased by 172,000, the unemployment rate held at 4.3%, labor-force participation was 61.8%, and average hourly earnings rose 0.3% month over month and 3.4% year over year.

May CPI increased 0.5% month over month and 4.2% year over year. Core CPI increased 0.2% month over month and 2.9% year over year. Energy increased 3.9% month over month and 23.5% year over year; shelter increased 0.3% month over month.

May PPI final demand increased 1.1% month over month and 6.5% year over year. PPI excluding foods, energy, and trade services increased 0.8% month over month and 5.1% year over year.

April PCE inflation was 0.4% month over month and 3.8% year over year. Core PCE was 0.2% month over month and 3.3% year over year. Personal income was essentially flat and PCE spending rose 0.5% month over month.

May advance retail and food services sales were $763.7 billion, up 0.9% month over month and 6.9% year over year. Retail trade sales were up 1.0% month over month and 7.5% year over year.

May industrial production edged up 0.1% month over month and was 1.7% above the year-earlier level. Manufacturing output was unchanged. Capacity utilization was 76.2%.

## Philadelphia Fed June Manufacturing Survey

The June 2026 Philadelphia Fed Manufacturing Business Outlook Survey was released June 18 at 8:30 a.m. ET and collected responses from June 8 through June 15.

| indicator | May | June |
| --- | ---: | ---: |
| general business activity | -0.4 | 10.3 |
| new orders | -1.7 | 27.3 |
| shipments | 4.9 | 14.9 |
| inventories | 6.6 | -8.5 |
| employment | -2.8 | 7.9 |
| average workweek | 1.2 | -6.5 |
| prices paid | 47.9 | 53.2 |
| prices received | 26.3 | 20.3 |
| future general activity | 53.2 | 50.2 |
| future new orders | 53.5 | 60.8 |
| future shipments | 45.7 | 60.3 |
| future prices paid | 70.0 | 63.2 |
| future prices received | 60.5 | 67.2 |
| future capital expenditures | 30.9 | 41.2 |

Special questions showed a larger share of firms reporting higher second-quarter production than lower production. Median capacity utilization was 70%-80% for 2026 Q2, unchanged from 2025 Q2.

## Housing

May housing starts were 1,177,000 SAAR, down 15.4% from April and down 8.7% from May 2025. Single-family starts were 882,000 SAAR and 5+ unit starts were 284,000 SAAR.

May building permits were 1,413,000 SAAR, down 0.7% from April and down 0.2% from May 2025. Single-family permits were 886,000 SAAR and 5+ unit permits were 474,000 SAAR. Completions were 1,313,000 SAAR.

## Generated Mechanical Return Context

CapitalBench generated a full 70-option trailing-return file for both June 18 rounds with no failed options. Selected rows from the generated one-week round file:

| asset proxy | symbol | adjusted close as of 2026-06-18 | 7d return | 30d return | 6m return | 1y return |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| S&P 500 | SPY | 746.74 | 1.48% | 2.03% | 11.30% | 26.75% |
| Nasdaq 100 | QQQ | 740.62 | 3.28% | 5.57% | 21.90% | 40.68% |
| US Small-Cap Stocks | IWM | 295.59 | 2.02% | 8.53% | 19.34% | 42.46% |
| Technology Sector | XLK | 191.44 | 4.49% | 10.51% | 35.62% | 59.36% |
| Semiconductors | SMH | 659.88 | 8.27% | 21.31% | 90.61% | 152.07% |
| Energy Sector | XLE | 53.77 | -5.86% | -12.27% | 23.67% | 26.02% |
| Crude Oil | USO | 114.87 | -10.84% | -24.90% | 70.96% | 39.63% |
| Gold | IAU | 79.33 | 0.25% | -5.92% | -2.82% | 24.97% |
| Silver | SLV | 59.51 | -2.15% | -11.05% | 0.32% | 78.87% |
| US Dollar | UUP | 28.30 | 1.25% | 1.84% | 4.61% | 6.71% |
| South Korea Equities | EWY | 219.20 | 10.18% | 25.96% | 143.37% | 230.32% |
| Taiwan Equities | EWT | 109.99 | 7.36% | 22.44% | 80.70% | 105.35% |
| Bitcoin ETF | IBIT | 35.62 | -1.19% | -18.11% | -25.73% | -39.60% |
| Ethereum ETF | ETHA | 12.88 | 1.42% | -19.15% | -38.67% | -31.78% |
| Short-Term Treasury Bills | BIL | 91.57 | 0.10% | 0.32% | 1.79% | 3.87% |
| Long-Term US Treasury Bonds | TLT | 86.75 | 0.90% | 4.90% | 0.59% | 4.69% |
| Cash / Do Not Invest | USD | 1.00 | 0.00% | 0.00% | 0.00% | 0.00% |

## In-Window Scheduled Dates

| date | event |
| --- | --- |
| 2026-06-19 | Juneteenth market holiday; Nasdaq and NYSE closed |
| 2026-06-25 | Weekly round exit close |
| 2026-06-25 | BEA Personal Income and Outlays, May 2026 |
| 2026-07-02 | BLS Employment Situation, June 2026 |
| 2026-07-14 | BLS CPI, June 2026 |
| 2026-07-15 | BLS PPI, June 2026 |
| 2026-07-16 | Census Advance Monthly Retail Trade Report, June 2026 |
| 2026-07-20 | Monthly round exit close |

FOMC July 28-29 is outside the monthly scoring window but remains listed in the broader official calendar.
