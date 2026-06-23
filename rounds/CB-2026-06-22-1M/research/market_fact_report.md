# Prompt 1 - Market Fact Report

Research cutoff: 2026-06-23T01:28:00Z

Rounds prepared from this report:

| round | horizon | entry date | exit date | decision deadline |
| --- | --- | --- | --- | --- |
| CB-2026-06-22-1W | one week | 2026-06-22 | 2026-06-29 | 2026-06-23T02:30:00Z |
| CB-2026-06-22-1M | one month | 2026-06-22 | 2026-07-22 | 2026-06-23T02:30:00Z |

## Source Ledger

Narrative facts were gathered manually from public web pages and official releases. No model API was used to generate these research artifacts. Tiingo was rate-limited while generating the mechanical market-data package, so CapitalBench generated the June 22 full-universe trailing-return and entry-price artifacts from Yahoo chart adjusted-close data and labeled those generated rows as `yahoo_chart_adjclose`.

| source | URL | facts used |
| --- | --- | --- |
| AP News, June 22 index close | https://apnews.com/article/wall-street-stocks-dow-nasdaq-15484e7e5b168601a3f2c0061eb3ffd1 | major U.S. index closes and year-to-date changes |
| AP News, June 22 market narrative | https://apnews.com/article/stocks-markets-us-iran-war-oil-690222f2e7005faf72b76daf46768b4d | oil move, Treasury yield, Big Tech weights, international market context |
| Federal Reserve FOMC statement, June 17 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm | target range and policy stance |
| Federal Reserve June 17 SEP accessible table | https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm | 2026 median projections and inflation-risk balance |
| Federal Reserve H.15 current release | https://www.federalreserve.gov/releases/h15/ | June 22 release, observations through June 19 because markets were closed June 19 |
| Department of Labor UI claims, June 18 PDF | https://www.dol.gov/ui/data.pdf | initial claims, insured unemployment, moving averages |
| Philadelphia Fed MBOS June 2026 | https://www.philadelphiafed.org/surveys-and-data/regional-economic-analysis/mbos-2026-06 | regional manufacturing current and future indexes |
| Census retail sales | https://www.census.gov/retail/sales.html | May 2026 advance retail sales |
| Census retail release schedule | https://www.census.gov/retail/release_schedule.html | July 16 release date for June 2026 advance retail trade |
| BLS CPI May release | https://www.bls.gov/news.release/cpi.nr0.htm | May CPI datapoints |
| BLS CPI release schedule | https://www.bls.gov/schedule/news_release/cpi.htm | July 14 release date for June CPI |
| BLS PPI May release | https://www.bls.gov/news.release/ppi.nr0.htm | May PPI datapoints and July 15 next release |
| BLS Employment Situation May release | https://www.bls.gov/news.release/empsit.nr0.htm | May payroll, unemployment, revisions |
| BLS Employment Situation schedule | https://www.bls.gov/schedule/news_release/empsit.htm | July 2 release date for June employment |
| BEA Personal Income and Outlays, April | https://www.bea.gov/news/2026/personal-income-and-outlays-april-2026 | April PCE, personal income, spending, next release date |
| BEA release schedule | https://www.bea.gov/news/schedule | June 24 and June 25 releases, July 7 trade, July 30 PCE/GDP releases |
| Federal Reserve G.17 industrial production | https://www.federalreserve.gov/releases/g17/current/default.htm | May industrial production and capacity utilization |
| Census new residential construction | https://www.census.gov/construction/nrc/current/index.html | May housing starts, permits, completions |
| Nasdaq market holiday schedule | https://www.nasdaq.com/market-activity/stock-market-holiday-schedule | July 3 Independence Day observed market closure |
| Federal Reserve FOMC calendar | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | July 28-29 FOMC meeting date |
| Generated CapitalBench market data | rounds/CB-2026-06-22-1W/market_data/universe_trailing_returns.csv | selected mechanical return context |
| Generated CapitalBench entry prices | rounds/CB-2026-06-22-1W/prices/entry_prices.csv | June 22 official entry prices |

## Market Close Snapshot

AP reported a mixed Monday, June 22 U.S. close after a three-day weekend. The S&P 500 slipped 0.4%, the Dow rose 0.3%, the Nasdaq Composite fell 1.3%, and the Russell 2000 rose 0.8%.

| index | June 22 close | daily change | year-to-date change |
| --- | ---: | ---: | ---: |
| S&P 500 | 7,472.79 | -27.79 / -0.4% | +627.29 / +9.2% |
| Dow Jones Industrial Average | 51,712.71 | +148.01 / +0.3% | +3,649.42 / +7.6% |
| Nasdaq Composite | 26,166.60 | -351.33 / -1.3% | +2,924.61 / +12.6% |
| Russell 2000 | 3,004.40 | +24.64 / +0.8% | +522.50 / +21.1% |

AP's market narrative said Brent crude fell 3.2% to $77.52 and U.S. crude fell 2.6% to $73.86 as weekend U.S.-Iran talks lowered oil-risk pricing. The same report said the 10-year Treasury yield climbed to 4.50% from 4.46% late Thursday and that Alphabet, Amazon, and Broadcom were among the heaviest S&P 500 weights. It also reported the United Kingdom's FTSE 100 rose 0.7%, Tokyo's Nikkei 225 rose 1.5% to another all-time high, and South Korea's Kospi rose 0.7% to its own record.

## Monetary Policy And Rates

The FOMC held the federal funds target range at 3.50%-3.75% on June 17, 2026. The June SEP median projections for 2026 were:

| projection | 2026 median |
| --- | ---: |
| real GDP growth | 2.2% |
| unemployment rate | 4.3% |
| PCE inflation | 3.6% |
| core PCE inflation | 3.3% |
| federal funds midpoint | 3.8% |

The SEP uncertainty and risk tables showed June inflation risks were heavily weighted to the upside: 17 participants weighted PCE inflation risk to the upside and 17 participants weighted core PCE inflation risk to the upside.

Federal Reserve H.15 was released June 22, 2026. Because markets were closed Friday, June 19, the latest market-yield column was June 18 for Treasury yields, while the effective federal funds rate column included June 19:

| rate | value | observation date |
| --- | ---: | --- |
| effective federal funds rate | 3.63% | 2026-06-19 |
| 3-month Treasury bill, secondary market | 3.67% | 2026-06-18 |
| 2-year Treasury constant maturity | 4.19% | 2026-06-18 |
| 5-year Treasury constant maturity | 4.23% | 2026-06-18 |
| 10-year Treasury constant maturity | 4.46% | 2026-06-18 |
| 30-year Treasury constant maturity | 4.90% | 2026-06-18 |
| 5-year TIPS real yield | 1.96% | 2026-06-18 |
| 10-year TIPS real yield | 2.21% | 2026-06-18 |

## Labor, Inflation, Consumption, And Production

The Department of Labor reported initial jobless claims of 226,000 for the week ended June 13, down 4,000 from the prior revised level of 230,000. The 4-week moving average was 223,250, up 4,000. Insured unemployment for the week ended June 6 was 1,810,000, up 24,000, and the insured unemployment rate was 1.2%.

May payrolls increased by 172,000, the unemployment rate held at 4.3%, and BLS revised March and April payrolls up by a combined 93,000.

May CPI increased 0.5% month over month and 4.2% year over year. Core CPI increased 0.2% month over month and 2.9% year over year. Energy increased 3.9% month over month and 23.5% year over year; shelter increased 0.3% month over month.

May PPI final demand increased 1.1% month over month and 6.5% year over year. PPI excluding foods, energy, and trade services increased 0.8% month over month and 5.1% year over year. Final-demand goods rose 2.8%, including a 10.7% increase in final-demand energy.

April PCE inflation was 0.4% month over month and 3.8% year over year. Core PCE was 0.2% month over month and 3.3% year over year. Personal income was essentially flat and PCE spending rose 0.5% month over month.

May advance retail and food services sales were $763.7 billion, up 0.9% month over month and 6.9% year over year. Retail trade sales were up 1.0% month over month and 7.5% year over year.

May industrial production edged up 0.1% month over month and was 1.7% above the year-earlier level. Manufacturing output was unchanged. Capacity utilization was 76.2%.

## Philadelphia Fed June Manufacturing Survey

The June 2026 Philadelphia Fed Manufacturing Business Outlook Survey was released June 18.

| indicator | May | June |
| --- | ---: | ---: |
| general business activity | -0.4 | 10.3 |
| new orders | -1.7 | 27.3 |
| shipments | 4.9 | 14.9 |
| inventories | 6.6 | -8.5 |
| employment | -2.8 | 7.9 |
| average workweek | 1.2 | -6.5 |
| future general activity | 53.2 | 50.2 |
| future new orders | 53.5 | 60.8 |
| future shipments | 45.7 | 60.3 |
| future prices paid | 70.0 | 63.2 |
| future prices received | 60.5 | 67.2 |
| future capital expenditures | 30.9 | 41.2 |

The release summary said current activity, new orders, and shipments were positive, price indicators still pointed to increases, and broad future indicators continued to suggest growth over the next six months.

## Housing

May housing starts were 1,177,000 SAAR, down 15.4% from April and down 8.7% from May 2025. Single-family starts were 882,000 SAAR and 5+ unit starts were 284,000 SAAR.

May building permits were 1,413,000 SAAR, down 0.7% from April and down 0.2% from May 2025. Single-family permits were 886,000 SAAR and 5+ unit permits were 474,000 SAAR. Completions were 1,313,000 SAAR.

## Generated Mechanical Return Context

CapitalBench generated a full 70-option trailing-return file for both June 22 rounds with no failed options. Selected rows from the generated one-week round file:

| asset proxy | symbol | adjusted close as of 2026-06-22 | 7d return | 30d return | 6m return | 1y return |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| S&P 500 | SPY | 744.39 | -1.13% | 0.09% | 9.27% | 26.65% |
| Nasdaq 100 | QQQ | 737.95 | -0.81% | 2.84% | 19.33% | 40.75% |
| US Small-Cap Stocks | IWM | 298.18 | 1.20% | 4.83% | 18.08% | 44.01% |
| Technology Sector | XLK | 192.15 | 0.19% | 6.52% | 32.54% | 60.68% |
| Semiconductors | SMH | 668.91 | 3.37% | 16.07% | 85.96% | 157.81% |
| Software | IGV | 87.31 | -5.79% | -7.11% | -19.85% | -16.92% |
| Energy Sector | XLE | 54.06 | -2.68% | -9.13% | 23.08% | 25.41% |
| Crude Oil | USO | 112.69 | -7.03% | -20.03% | 61.61% | 35.58% |
| Gold | IAU | 78.80 | -3.03% | -7.09% | -5.73% | 24.19% |
| Silver | SLV | 58.91 | -7.18% | -13.82% | -5.70% | 80.04% |
| US Dollar | UUP | 28.36 | 1.39% | 2.12% | 4.92% | 7.04% |
| South Korea Equities | EWY | 219.02 | 3.58% | 20.32% | 138.71% | 226.78% |
| Taiwan Equities | EWT | 111.53 | 4.85% | 15.17% | 79.95% | 112.72% |
| Bitcoin ETF | IBIT | 36.50 | -3.29% | -15.04% | -27.13% | -37.79% |
| Ethereum ETF | ETHA | 13.06 | -5.09% | -16.12% | -41.90% | -28.52% |
| Short-Term Treasury Bills | BIL | 91.57 | 0.07% | 0.27% | 1.75% | 3.85% |
| Long-Term US Treasury Bonds | TLT | 86.09 | 0.43% | 2.06% | 0.41% | 4.08% |
| Cash / Do Not Invest | USD | 1.00 | 0.00% | 0.00% | 0.00% | 0.00% |

## In-Window Scheduled Dates

| date | event |
| --- | --- |
| 2026-06-24 | BEA U.S. International Transactions and Investment Position, Q1 2026 and annual update |
| 2026-06-25 | BEA GDP third estimate, industries, corporate profits, state GDP, and state personal income, Q1 2026 |
| 2026-06-25 | BEA Personal Income and Outlays, May 2026 |
| 2026-06-29 | Weekly round exit close |
| 2026-07-02 | BLS Employment Situation, June 2026 |
| 2026-07-03 | Independence Day observed; Nasdaq and NYSE closed |
| 2026-07-07 | BEA U.S. International Trade in Goods and Services, May 2026 |
| 2026-07-14 | BLS CPI, June 2026 |
| 2026-07-15 | BLS PPI, June 2026 |
| 2026-07-16 | Census Advance Monthly Retail Trade Report, June 2026 |
| 2026-07-22 | Monthly round exit close |

FOMC July 28-29 is outside the monthly scoring window but remains listed in the broader official calendar.
