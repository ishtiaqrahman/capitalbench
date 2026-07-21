# Prompt 1 Market Fact Report

Round: CB-2026-07-20-1W
Horizon: one week, July 20 through July 27, 2026 adjusted close
Research cutoff: 2026-07-21T00:10:00Z
Status: audit-only; not model-facing

## Scope And Method

This report records fixed facts publicly available by the research cutoff. I prepared it through direct navigation and review of public webpages in a real browser. No participant-model API, model agent, search API, provider-hosted search, or model-generated research was used. Facts are not ranked and are not mapped to CapitalBench options.

The BLS webpages returned an access-denied response during this browser session. The latest BLS figures below therefore retain the previously published official release values and URLs, and the access limitation is disclosed rather than treated as a fresh page observation. Other official and news sources were opened and reviewed directly during this session.

Mechanical price, return, volume, volatility, drawdown, beta, correlation, and 52-week-position data are maintained separately in `market_data/universe_decision_context.md`. The complete generated artifact covers the frozen universe in option order and stops at the July 20 close. No selected return subset is reproduced here.

## Source Ledger

### 1. June Consumer And Producer Prices

- Publisher: U.S. Bureau of Labor Statistics
- Publication dates: July 14 and July 15, 2026
- Observation period: June 2026
- URLs: https://www.bls.gov/news.release/archives/cpi_07142026.htm and https://www.bls.gov/news.release/archives/ppi_07152026.htm
- Fixed facts: All-items CPI decreased 0.4% on a seasonally adjusted monthly basis and increased 3.5% over 12 months; energy decreased 5.7%; CPI excluding food and energy was unchanged for the month and increased 2.6% over 12 months. Final-demand producer prices decreased 0.3% for the month and increased 5.5% over 12 months; goods decreased 1.4%, including a 6.4% energy decrease, while services increased 0.2%.
- Source-reported status or uncertainty: CPI monthly changes are seasonally adjusted and 12-month changes are not. June PPI values are preliminary and subject to revision. The source pages returned access denied in the current browser session.

### 2. June Import And Export Prices

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 17, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/ximpim.nr0.htm
- Fixed facts: Import prices increased 0.3% in June and 7.1% over 12 months. Nonfuel import prices increased 0.4% for the month and 4.2% over 12 months. Export prices decreased 0.6% for the month.
- Source-reported status or uncertainty: These indexes are subject to revision in later monthly releases. The source page returned access denied in the current browser session.

### 3. June Employment Situation

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 2, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/empsit.nr0.htm
- Fixed facts: Nonfarm payroll employment increased by 57,000 and unemployment was 4.2%. April and May payroll changes were revised down by a combined 74,000. Average hourly earnings increased 0.3% in June and 3.5% over 12 months. Labor-force participation was 61.5%.
- Source-reported status or uncertainty: Establishment estimates are revised as additional reports and recalculated seasonal factors become available. The source page returned access denied in the current browser session.

### 4. June Retail Sales

- Publisher: U.S. Census Bureau
- Publication date: July 16, 2026
- Observation period: June 2026
- URL: https://www.census.gov/retail/sales.html
- Fixed facts: Advance retail and food-services sales were $768.6 billion, up 0.2% from May and 6.7% from June 2025. April-through-June sales were up 6.4% from the same period a year earlier. May's monthly change was revised to 1.0% from 0.9%.
- Source-reported uncertainty: The monthly change was 0.2% plus or minus 0.4 percentage point and the year-over-year change was 6.7% plus or minus 0.5 percentage point, both at 90% confidence.

### 5. June Industrial Production

- Publisher: Board of Governors of the Federal Reserve System
- Publication date: July 17, 2026
- Observation period: June and second quarter 2026
- URL: https://www.federalreserve.gov/releases/g17/current/default.htm
- Fixed facts: Industrial production increased 0.1% in June and at a 4.0% annual rate in the second quarter. Manufacturing output was unchanged in June and grew at a 4.7% annual rate in the quarter. Capacity utilization was 76.1%, 3.3 percentage points below its 1972-2025 average.
- Source-reported status or uncertainty: June values are preliminary. An annual revision is planned for autumn 2026.

### 6. First-Quarter GDP And May Personal Income And Outlays

- Publisher: U.S. Bureau of Economic Analysis
- Publication date: June 25, 2026
- Observation periods: first quarter and May 2026
- URLs: https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-1st and https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026
- Fixed facts: Third-estimate real GDP increased at a 2.1% annual rate and real final sales to private domestic purchasers increased 1.7%. In May, real PCE increased 0.3%; the PCE price index increased 0.4% for the month and 4.1% over 12 months; core PCE increased 0.3% for the month and 3.4% over 12 months; the saving rate was 3.0%.
- Source-reported status or uncertainty: BEA estimates are revised as more complete source data become available.

### 7. Federal Reserve Decision, Projections, And Calendar

- Publisher: Board of Governors of the Federal Reserve System
- Publication dates: June 17, 2026; calendar last updated July 8, 2026
- Observation and forecast period: June decision, 2026 projections, and July meeting schedule
- URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm and https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm and https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- Fixed facts: The FOMC maintained the federal-funds target range at 3.5% to 3.75% by a 12-0 vote. Participant medians for 2026 were 2.2% real GDP growth, 4.3% unemployment, 3.6% PCE inflation, 3.3% core PCE inflation, and a 3.8% year-end federal-funds rate. The next scheduled meeting is July 28-29, after the weekly exit.
- Source-reported status or uncertainty: Projections are individual participant assessments, not a Committee plan.

### 8. Treasury Yield Curve

- Publisher: U.S. Department of the Treasury
- Publication and observation date: July 20, 2026
- URL: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve
- Fixed facts: Nominal constant-maturity yields were 3.86% at three months, 4.21% at two years, 4.60% at ten years, and 5.11% at 30 years.
- Source-reported status or uncertainty: Treasury rates are interpolated from indicative bid-side prices at approximately 3:30 p.m. ET and are not transaction yields for one security.

### 9. July 20 U.S. Market Close

- Publisher: Associated Press
- Publication and observation date: July 20, 2026; updated 4:50 p.m. ET
- URL: https://apnews.com/article/stocks-market-ai-oil-iran-war-15939a01f378bcec5eec2868e8100ca9
- Fixed facts: The S&P 500 fell 14.41 points, or 0.2%, to 7,443.28. The Dow fell 307.16 points, or 0.6%, to 51,839.26. The Nasdaq Composite fell 12.17 points, less than 0.1%, to 25,508.07. The report stated that a majority of U.S. stocks fell. Nvidia rose 0.2%, Sandisk rose 2.7%, and AMD rose 1.6%.
- Source-reported status or uncertainty: Values are an end-of-session news report and can differ from later vendor corrections; no numerical breadth ratio was reported.

### 10. July 20 Energy And International Market Facts

- Publisher: Associated Press
- Publication and observation date: July 20, 2026
- URL: https://apnews.com/article/stocks-market-ai-oil-iran-war-15939a01f378bcec5eec2868e8100ca9
- Fixed facts: Brent crude settled at $89.22 per barrel, up 1.3% for the day. S&P Global counted 127 vessels passing through the Strait of Hormuz in the week through July 19, nearly 50% fewer than the prior week. South Korea's Kospi fell 4.5%, while Hong Kong rose 2.4% and Shanghai rose 0.9%.
- Source-reported status or uncertainty: Shipping data were attributed by AP to S&P Global. Cross-market figures are contemporaneous market-report values.

### 11. China First-Half Activity

- Publisher: National Bureau of Statistics of China
- Publication date: July 15, 2026
- Observation period: second quarter, June, and first half 2026
- URL: https://www.stats.gov.cn/english/PressRelease/202607/t20260715_1964120.html
- Fixed facts: First-half real GDP increased 4.7% year over year; second-quarter GDP increased 4.3% year over year and 0.9% quarter over quarter. June industrial value added increased 5.3% year over year and 0.76% month over month. The official manufacturing PMI was 50.3.
- Source-reported status or uncertainty: GDP figures were preliminary. Month-over-month series are seasonally adjusted and subject to revision.

### 12. Energy Forecast

- Publisher: U.S. Energy Information Administration
- Publication date: July 7, 2026
- Observation and forecast periods: June, third quarter 2026, and full-year 2026
- URL: https://www.eia.gov/pressroom/releases/press590.php
- Fixed facts: EIA reported that Brent crude averaged $85 per barrel in June and forecast a $74 third-quarter average. It forecast 2026 U.S. crude production of 13.8 million barrels per day, Henry Hub natural gas at $3.67 per MMBtu, and retail gasoline at $3.64 per gallon.
- Source-reported status or uncertainty: Forecasts are from the July Short-Term Energy Outlook and can change.

### 13. Scheduled Weekly Catalysts

- Publishers: U.S. Bureau of Economic Analysis; U.S. Bureau of Labor Statistics; U.S. Energy Information Administration; Associated Press
- Calendar and publication review date: July 20, 2026
- URLs: https://www.bea.gov/news/schedule and https://www.bls.gov/schedule/2026/07_sched.htm and https://www.eia.gov/petroleum/supply/weekly/ and https://apnews.com/article/stocks-market-ai-oil-iran-war-15939a01f378bcec5eec2868e8100ca9
- Fixed facts: BEA scheduled Direct Investment by Country and Industry for July 21 at 8:30 a.m. ET. BLS had scheduled June state employment and second-quarter usual weekly earnings for July 21 at 10:00 a.m. ET. Alphabet was scheduled to report earnings July 22. EIA's weekly petroleum report is scheduled for July 22 at 10:30 a.m. ET.
- Source-reported status or uncertainty: Scheduled dates and times can change. The BLS calendar returned access denied in the current browser session.

## Prompt 1 Completion Check

- Facts stop at the research cutoff: yes.
- Direct public-source browser review used and access limitations disclosed: yes.
- URLs, publishers, publication dates, observation dates, and source-reported uncertainty retained here: yes.
- Current macro releases, rates, index closes, broad breadth status, international and energy data, and in-window catalysts covered: yes.
- Complete mechanical artifact referenced without selecting return rows: yes.
- Rankings, allocations, recommendations, and affected-option mapping: none.
