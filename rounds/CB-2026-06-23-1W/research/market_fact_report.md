# Prompt 1 - Market Fact Report

Research cutoff: 2026-06-23T21:20:00Z

Rounds prepared from this report:

| round | horizon | entry date | exit date | decision deadline |
| --- | --- | --- | --- | --- |
| CB-2026-06-23-1W | one week | 2026-06-23 | 2026-06-30 | 2026-06-24T02:30:00Z |
| CB-2026-06-23-1M | one month | 2026-06-23 | 2026-07-23 | 2026-06-24T02:30:00Z |

## Source Ledger

Narrative facts were gathered manually from public web pages and official releases. No model API was used to generate these research artifacts. CapitalBench generated the June 23 full-universe trailing-return artifacts from market-data fetches before this report was finalized. The entry-price files were derived from the same frozen `as_of_adj_close` values in those full-universe artifacts after the direct entry-price fetch hit an HTTP 429 rate limit.

| source | URL | facts used |
| --- | --- | --- |
| AP News, June 23 index close | https://apnews.com/article/8a525396331d3cf41e9a341026c005e7 | major U.S. index closes, daily changes, week-to-date changes, and year-to-date changes |
| AP News, June 23 market narrative | https://apnews.com/article/03c6efaefd208a4b68679cdccde51cf9 | Big Tech and AI-linked selloff, semiconductor moves, breadth context, and rate-expectation context |
| Federal Reserve FOMC statement, June 17 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm | target range and policy stance |
| Federal Reserve H.15 current release | https://www.federalreserve.gov/releases/h15/ | June 23 release and June 22 rate observations |
| BLS CPI May release | https://www.bls.gov/news.release/cpi.nr0.htm | May CPI datapoints |
| Census retail sales | https://www.census.gov/retail/sales.html | May 2026 advance retail sales |
| BEA release schedule | https://www.bea.gov/news/schedule | June 24, June 25, July 7, and July 30 scheduled releases |
| Nasdaq market holiday schedule | https://www.nasdaq.com/market-activity/stock-market-holiday-schedule | July 3 Independence Day observed market closure |
| Generated CapitalBench market data | rounds/CB-2026-06-23-1W/market_data/universe_trailing_returns.csv | selected mechanical return context |
| Generated CapitalBench entry prices | rounds/CB-2026-06-23-1W/prices/entry_prices.csv | June 23 official entry prices derived from the frozen full-universe table |

## Market Close Snapshot

AP reported a Tuesday, June 23 U.S. close led lower by Big Tech and AI-linked shares. The S&P 500 fell 1.4%, the Nasdaq Composite fell 2.2%, the Dow fell 0.1%, and the Russell 2000 fell 1.0%.

| index | June 23 close | daily change | week-to-date change | year-to-date change |
| --- | ---: | ---: | ---: | ---: |
| S&P 500 | 7,365.46 | -107.33 / -1.4% | -1.8% | +7.6% |
| Dow Jones Industrial Average | 51,666.84 | -45.87 / -0.1% | +0.2% | +7.5% |
| Nasdaq Composite | 25,587.04 | -579.56 / -2.2% | -3.5% | +10.1% |
| Russell 2000 | 2,975.48 | -28.92 / -1.0% | -0.1% | +19.9% |

AP's market narrative said more S&P 500 stocks rose than fell, while the largest technology weights pulled the capitalization-weighted index lower. The report said Micron fell 13.2%, Nvidia fell 4.1%, Samsung Electronics in South Korea fell 12.3%, and South Korea's Kospi fell 10.0%.

## Monetary Policy And Rates

The FOMC held the federal funds target range at 3.50%-3.75% on June 17, 2026.

Federal Reserve H.15 was released June 23, 2026. Selected June 22 observations:

| rate | value | observation date |
| --- | ---: | --- |
| effective federal funds rate | 3.63% | 2026-06-22 |
| 3-month Treasury bill, secondary market | 3.70% | 2026-06-22 |
| 2-year Treasury constant maturity | 4.24% | 2026-06-22 |
| 5-year Treasury constant maturity | 4.29% | 2026-06-22 |
| 10-year Treasury constant maturity | 4.51% | 2026-06-22 |
| 30-year Treasury constant maturity | 4.95% | 2026-06-22 |
| 5-year TIPS real yield | 2.01% | 2026-06-22 |
| 10-year TIPS real yield | 2.28% | 2026-06-22 |

## Inflation And Consumption

May CPI increased 0.5% month over month and 4.2% year over year. Core CPI increased 0.2% month over month and 2.9% year over year. Energy increased 3.9% month over month and 23.5% year over year; shelter increased 0.3% month over month.

May advance retail and food services sales were $763.7 billion, up 0.9% month over month and 6.9% year over year. Retail trade sales were up 1.0% month over month and 7.5% year over year.

## Generated Mechanical Return Context

CapitalBench generated a full 70-option trailing-return file for both June 23 rounds with no failed options. Selected rows from the generated one-week round file:

| asset proxy | symbol | adjusted close as of 2026-06-23 | 7d return | 30d return | 6m return | 1y return |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Cash / Do Not Invest | USD | 1.00 | 0.00% | 0.00% | 0.00% | 0.00% |
| Short-Term Treasury Bills | BIL | 91.58 | 0.07% | 0.28% | 1.76% | 3.84% |
| S&P 500 | SPY | 733.58 | -1.98% | -1.37% | 7.20% | 23.58% |
| Nasdaq 100 | QQQ | 713.65 | -2.11% | -0.43% | 14.98% | 34.88% |
| US Small-Cap Stocks | IWM | 295.32 | 1.11% | 3.82% | 17.64% | 40.90% |
| Technology Sector | XLK | 184.19 | -1.09% | 2.23% | 26.50% | 52.46% |
| Semiconductors | SMH | 622.05 | 0.98% | 7.93% | 71.29% | 138.23% |
| Software | IGV | 87.32 | -4.43% | -7.10% | -19.19% | -17.89% |
| Energy Sector | XLE | 54.46 | -0.93% | -7.80% | 24.05% | 30.52% |
| Crude Oil | USO | 111.26 | -3.65% | -21.05% | 58.26% | 45.61% |
| Gold | IAU | 77.33 | -5.12% | -8.82% | -8.68% | 21.45% |
| Silver | SLV | 55.73 | -12.08% | -18.48% | -14.05% | 69.08% |
| US Dollar | UUP | 28.45 | 1.86% | 2.45% | 5.61% | 7.81% |
| South Korea Equities | EWY | 192.20 | -6.66% | 5.59% | 107.34% | 183.17% |
| Taiwan Equities | EWT | 105.24 | 1.40% | 8.67% | 68.38% | 99.48% |
| Bitcoin ETF | IBIT | 35.31 | -5.00% | -17.81% | -28.88% | -39.82% |
| Ethereum ETF | ETHA | 12.52 | -7.53% | -19.59% | -44.16% | -28.54% |
| Long-Term US Treasury Bonds | TLT | 86.20 | 0.01% | 2.20% | 0.38% | 3.88% |

## In-Window Scheduled Dates

| date | event |
| --- | --- |
| 2026-06-24 | BEA U.S. International Transactions and Investment Position, Q1 2026 and annual update |
| 2026-06-25 | BEA GDP third estimate, industries, corporate profits, state GDP, and state personal income, Q1 2026 |
| 2026-06-25 | BEA Personal Income and Outlays, May 2026 |
| 2026-06-30 | Weekly round exit close |
| 2026-07-03 | Independence Day observed; Nasdaq and NYSE closed |
| 2026-07-07 | BEA U.S. International Trade in Goods and Services, May 2026 |
| 2026-07-23 | Monthly round exit close |
| 2026-07-30 | BEA GDP advance estimate for Q2 2026 and Personal Income and Outlays, June 2026 |
