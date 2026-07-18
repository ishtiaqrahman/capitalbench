# Prompt 1 Market Fact Report

Round: CB-2026-07-17-1W
Horizon: one week, July 17 through July 24, 2026 adjusted close
Research cutoff: 2026-07-18T06:20:00Z
Status: audit-only; not model-facing

## Scope And Method

This report records fixed facts publicly available by the research cutoff. Research was performed through direct browsing and review of public source pages. No participant-model API, provider search feature, or model-generated research was used. Facts are not ranked and are not mapped to CapitalBench options.

Mechanical price, return, volume, volatility, drawdown, beta, correlation, and 52-week-position data are maintained separately in `market_data/universe_decision_context.md`. The complete generated artifact covers the frozen universe in option order and stops at the July 17 close. No selected return subset is reproduced here.

## Source Ledger

### 1. June Consumer Price Index

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 14, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/archives/cpi_07142026.htm
- Fixed facts: All-items CPI decreased 0.4% on a seasonally adjusted monthly basis and increased 3.5% over 12 months. Energy decreased 5.7% in June. CPI excluding food and energy was unchanged in June and increased 2.6% over 12 months.
- Source-reported status or uncertainty: Monthly changes are seasonally adjusted; 12-month changes are not seasonally adjusted. The chained CPI for the prior 10 to 12 months is subject to revision.

### 2. June Producer Price Index

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 15, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/archives/ppi_07152026.htm
- Fixed facts: Final-demand prices decreased 0.3% in June and increased 5.5% over 12 months. Final-demand goods decreased 1.4%, including a 6.4% decrease in energy, while final-demand services increased 0.2%. Final demand excluding food, energy, and trade services increased 0.1% in June and 5.1% over 12 months.
- Source-reported status or uncertainty: June values are preliminary and PPI data are subject to revision four months after original publication.

### 3. June Import And Export Prices

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 17, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/ximpim.nr0.htm
- Fixed facts: Import prices increased 0.3% in June and 7.1% over 12 months. Nonfuel import prices increased 0.4% in June and 4.2% over 12 months. Export prices decreased 0.6% in June after increasing 1.2% in May.
- Source-reported status or uncertainty: Import and export price indexes are subject to revision in subsequent monthly releases.

### 4. June Employment Situation

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 2, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/empsit.nr0.htm
- Fixed facts: Nonfarm payroll employment increased by 57,000 and unemployment was 4.2%. April and May payroll changes were revised down by a combined 74,000. Average hourly earnings increased 0.3% in June and 3.5% over 12 months. Labor-force participation decreased 0.3 percentage point to 61.5%.
- Source-reported status or uncertainty: Establishment estimates are revised when additional reports and recalculated seasonal factors become available.

### 5. June Retail Sales

- Publisher: U.S. Census Bureau
- Publication date: July 16, 2026
- Observation period: June 2026
- URL: https://www.census.gov/retail/sales.html
- Fixed facts: Advance retail and food-services sales were $768.6 billion, up 0.2% from May and 6.7% from June 2025. April-through-June sales were up 6.4% from the same period a year earlier. May's monthly change was revised to 1.0% from 0.9%.
- Source-reported uncertainty: The monthly change was 0.2% plus or minus 0.4 percentage point and the year-over-year change was 6.7% plus or minus 0.5 percentage point, both at 90% confidence.

### 6. June Industrial Production And Capacity Utilization

- Publisher: Board of Governors of the Federal Reserve System
- Publication date: July 17, 2026
- Observation period: June and second quarter 2026
- URL: https://www.federalreserve.gov/releases/g17/current/default.htm
- Fixed facts: Industrial production increased 0.1% in June and at a 4.0% annual rate in the second quarter. Manufacturing output was unchanged in June and increased at a 4.7% annual rate in the quarter. Total capacity utilization was unchanged at 76.1%, 3.3 percentage points below its 1972-2025 average.
- Source-reported status or uncertainty: June values are preliminary. The Federal Reserve plans an annual revision in autumn 2026.

### 7. First-Quarter GDP And May Personal Income And Outlays

- Publisher: U.S. Bureau of Economic Analysis
- Publication dates: June 25 and June 26, 2026
- Observation periods: first quarter and May 2026
- URLs: https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-1st and https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026
- Fixed facts: Third-estimate real GDP increased at a 2.1% annual rate and real final sales to private domestic purchasers increased 1.7%. In May, real PCE increased 0.3%, the PCE price index increased 0.4% for the month and 4.1% over 12 months, core PCE increased 0.3% for the month and 3.4% over 12 months, and the saving rate was 3.0%.
- Source-reported status or uncertainty: BEA estimates are revised as more complete source data become available.

### 8. June Federal Reserve Decision And Projections

- Publisher: Board of Governors of the Federal Reserve System
- Publication date: June 17, 2026
- Observation and forecast period: June decision and 2026 projections
- URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm and https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm
- Fixed facts: The FOMC maintained the federal-funds target range at 3.5% to 3.75% by a 12-0 vote. Participant medians for 2026 were 2.2% real GDP growth, 4.3% unemployment, 3.6% PCE inflation, 3.3% core PCE inflation, and a 3.8% year-end federal-funds rate.
- Source-reported status or uncertainty: Projections are individual participant assessments, not a Committee plan. Seventeen of 18 participants assessed PCE-inflation uncertainty as higher than the prior-20-year average and risks as weighted to the upside.

### 9. Treasury Yield Curve

- Publisher: U.S. Department of the Treasury
- Publication and observation date: July 17, 2026
- URL: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve
- Fixed facts: Nominal constant-maturity yields were 3.85% at three months, 4.18% at two years, 4.55% at ten years, and 5.06% at 30 years.
- Source-reported status or uncertainty: Treasury curve rates are interpolated from actively traded market securities and are not transaction yields for one security.

### 10. July 17 U.S. Market Close And Breadth

- Publishers: Associated Press; Reuters via MarketScreener
- Publication and observation date: July 17, 2026
- URLs: https://apnews.com/article/wall-street-stocks-dow-nasdaq-5e44034ea86fa8d9c73184f3559e74a2 and https://in.marketscreener.com/news/wall-st-slides-as-ai-rally-worries-deepen-ce7f51dada89ff25
- Fixed facts: The S&P 500 closed at 7,475.69, down 1.0% for the session and 1.6% for the week. The Nasdaq Composite closed at 25,520.24, down 1.4% for the session and 2.9% for the week. The Russell 2000 closed at 2,962.22, down 0.4% for the session and 0.5% for the week. Declining issues outnumbered advancers by 1.76 to 1 on the NYSE and 1.73 to 1 on Nasdaq. Brent crude increased 4.6% for the session.
- Source-reported status or uncertainty: Index values and breadth counts are end-of-session market reports and can differ from later vendor corrections.

### 11. China First-Half Activity

- Publisher: National Bureau of Statistics of China
- Publication dates: July 15-17, 2026
- Observation period: second quarter, June, and first half 2026
- URLs: https://www.stats.gov.cn/english/PressRelease/202607/t20260715_1964120.html and https://www.stats.gov.cn/english/PressRelease/202607/t20260716_1964159.html and https://www.stats.gov.cn/english/PressRelease/202607/t20260701_1964047.html
- Fixed facts: First-half real GDP increased 4.7% year over year; second-quarter GDP increased 4.3% year over year and 0.9% quarter over quarter. June industrial value added increased 5.3% year over year and 0.76% month over month. The official manufacturing PMI was 50.3; its small-enterprise component was 48.2.
- Source-reported status or uncertainty: GDP figures were preliminary. Month-over-month series are seasonally adjusted and subject to automatic revision.

### 12. Energy Data And Forecast

- Publisher: U.S. Energy Information Administration
- Publication dates: July 7 and July 15, 2026
- Observation and forecast periods: June, third quarter 2026, and week ending July 10
- URLs: https://www.eia.gov/pressroom/releases/press590.php and https://www.eia.gov/petroleum/supply/weekly/
- Fixed facts: EIA reported Brent crude averaged $85 per barrel in June and forecast a $74 third-quarter average. It forecast 2026 U.S. crude production of 13.8 million barrels per day and a $3.67 per MMBtu Henry Hub average. The latest weekly petroleum report covered the week ending July 10.
- Source-reported status or uncertainty: Forecasts were completed for the July Short-Term Energy Outlook and can change. Weekly petroleum estimates are preliminary.

## Scheduled Catalysts Inside The Weekly Scoring Window

- July 21 at 8:30 a.m. ET: BEA Direct Investment by Country and Industry for 2025.
- July 21 at 10:00 a.m. ET: BLS State Employment and Unemployment for June and Usual Weekly Earnings for the second quarter.
- July 22 at 10:30 a.m. ET: EIA Weekly Petroleum Status Report for the week ending July 17.
- July 24: weekly exit snapshot uses adjusted closes after regular trading ends.

## Prompt 1 Completion Check

- Facts stop at the research cutoff: yes.
- Direct public-source review used: yes.
- URLs, publishers, publication dates, observation dates, and reported uncertainty retained here: yes.
- Current macro releases, rates, index closes, breadth, international and energy data, and in-window catalysts covered: yes.
- Complete mechanical artifact referenced without selecting return rows: yes.
- Rankings, allocations, option recommendations, and affected-option mapping: none.
