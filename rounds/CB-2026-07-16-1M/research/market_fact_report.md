# Prompt 1 Market Fact Report

Round: CB-2026-07-16-1M
Horizon: one month, July 16 through August 14, 2026 adjusted close
Research cutoff: 2026-07-17T10:15:00Z
Status: audit-only; not model-facing

## Scope And Method

This report records fixed facts that were publicly available by the research cutoff. Research was performed through direct browsing of public, primary-source pages. No participant-model API, provider search tool, or model-generated web research was used. Facts are not ranked or mapped to CapitalBench options.

Mechanical price, return, volume, volatility, drawdown, beta, correlation, and 52-week-position data are maintained separately in `market_data/universe_decision_context.md`. That complete artifact covers all 70 frozen options, is ordered by frozen option order rather than performance, stops at the July 16 close, and was generated from Yahoo chart adjusted closes and reported volume with zero failed options. No selected return subset is reproduced here.

## Source Ledger

### 1. June Consumer Price Index

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 14, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/cpi.htm
- Fixed facts: The all-items CPI decreased 0.4% on a seasonally adjusted monthly basis and increased 3.5% over 12 months. The energy index decreased 5.7% in June. CPI excluding food and energy was unchanged in June and increased 2.6% over 12 months.
- Source-reported status or uncertainty: BLS seasonally adjusts monthly changes; 12-month changes are not seasonally adjusted.

### 2. June Producer Price Index

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 15, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/archives/ppi_07152026.htm
- Fixed facts: Final-demand prices decreased 0.3% in June and increased 5.5% over 12 months. Final-demand goods decreased 1.4%, including a 6.4% decrease in energy, while final-demand services increased 0.2%. Final demand excluding food, energy, and trade services increased 0.1% in June and 5.1% over 12 months.
- Source-reported status or uncertainty: PPI data are subject to revision four months after original publication.

### 3. June Employment Situation

- Publisher: U.S. Bureau of Labor Statistics
- Publication date: July 2, 2026
- Observation period: June 2026
- URL: https://www.bls.gov/news.release/empsit.nr0.htm
- Fixed facts: Nonfarm payroll employment increased by 57,000 and the unemployment rate was 4.2%. April and May payroll changes were revised down by a combined 74,000. Average hourly earnings increased 0.3% in June and 3.5% over 12 months. The labor-force participation rate decreased 0.3 percentage point to 61.5%.
- Source-reported status or uncertainty: Establishment-survey estimates are revised when additional reports and recalculated seasonal factors become available.

### 4. June Advance Retail Sales

- Publisher: U.S. Census Bureau
- Publication date: July 16, 2026
- Observation period: June 2026
- URL: https://www.census.gov/retail/sales.html
- Fixed facts: Advance retail and food-services sales were $768.6 billion, up 0.2% from May and 6.7% from June 2025. Sales for April through June were up 6.4% from the same period a year earlier. May's monthly change was revised to 1.0% from 0.9%.
- Source-reported uncertainty: The monthly change was reported as 0.2% plus or minus 0.4 percentage point; the year-over-year change as 6.7% plus or minus 0.5; and the three-month change as 6.4% plus or minus 0.5, all at the 90% confidence level.

### 5. First-Quarter GDP, Third Estimate

- Publisher: U.S. Bureau of Economic Analysis
- Publication date: June 25, 2026
- Observation period: first quarter 2026
- URL: https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-1st
- Fixed facts: Real GDP increased at a 2.1% annual rate. Real final sales to private domestic purchasers increased 1.7%. Real gross domestic income increased 1.2%, and the average of real GDP and real GDI increased 1.7%. Corporate profits increased $74.4 billion. The PCE price index increased at a 4.6% annual rate and the index excluding food and energy increased 4.4%.
- Source-reported status or uncertainty: This was the third estimate and incorporates more complete source data than the prior estimate.

### 6. May Personal Income And Outlays

- Publisher: U.S. Bureau of Economic Analysis
- Publication date: June 26, 2026
- Observation period: May 2026
- URL: https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026
- Fixed facts: Personal income increased 0.7%, current-dollar personal consumption expenditures increased 0.7%, and real PCE increased 0.3%. The PCE price index increased 0.4% for the month and 4.1% over 12 months. Excluding food and energy, it increased 0.3% for the month and 3.4% over 12 months. The personal saving rate was 3.0%.
- Source-reported status or uncertainty: BEA estimates are revised as more complete source data become available.

### 7. June Federal Reserve Decision

- Publisher: Board of Governors of the Federal Reserve System
- Publication date: June 17, 2026
- Observation date: June 17, 2026
- URL: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
- Fixed facts: The FOMC maintained the federal-funds target range at 3.5% to 3.75% by a 12-0 vote. The statement described economic activity as expanding at a solid pace, said productivity and business fixed investment had continued to rise, and said inflation remained elevated.
- Source-reported status or uncertainty: The Committee stated that future adjustments would depend on incoming data, the evolving outlook, and the balance of risks.

### 8. June Federal Reserve Projections And Minutes

- Publisher: Board of Governors of the Federal Reserve System
- Publication dates: June 17 and July 8, 2026
- Observation period: June 16-17 meeting and 2026 projections
- URLs: https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm and https://www.federalreserve.gov/monetarypolicy/fomcminutes20260617.htm
- Fixed forecast medians for 2026: real GDP growth 2.2%, unemployment 4.3%, PCE inflation 3.6%, core PCE inflation 3.3%, and year-end federal-funds rate 3.8%. The minutes recorded elevated uncertainty related to commodity prices and supply disruptions and data-dependent views on future policy actions.
- Source-reported uncertainty: Seventeen of 18 participants assessed uncertainty around PCE inflation as higher than the average of the prior 20 years, and 17 assessed inflation risks as weighted to the upside. The projections are individual participant assessments, not a Committee plan.

### 9. Treasury Yield Curve

- Publisher: U.S. Department of the Treasury
- Publication date: July 16, 2026
- Observation date: July 16, 2026
- URL: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve
- Fixed facts: Constant-maturity nominal yields were 3.84% at three months, 4.16% at two years, 4.57% at ten years, and 5.09% at 30 years. Real constant-maturity yields were 2.04% at five years, 2.35% at ten years, and 2.91% at 30 years.
- Source-reported status or uncertainty: Treasury curve rates are interpolated from actively traded market securities and are not transaction yields for a single security.

### 10. China First-Half Activity

- Publisher: National Bureau of Statistics of China
- Publication date: July 15, 2026
- Observation period: second quarter, June, and first half of 2026
- URL: https://www.stats.gov.cn/english/PressRelease/202607/t20260715_1964120.html
- Fixed facts: Real GDP increased 4.7% year over year in the first half. Second-quarter GDP increased 4.3% year over year and 0.9% quarter over quarter. June industrial value added increased 5.3% year over year and 0.76% month over month.
- Source-reported status or uncertainty: GDP figures were preliminary estimates; month-over-month series are seasonally adjusted and subject to automatic revision.

### 11. China June PMI And Producer Prices

- Publisher: National Bureau of Statistics of China
- Publication dates: July 1 and July 10, 2026
- Observation period: June 2026
- URLs: https://www.stats.gov.cn/english/PressRelease/202607/t20260701_1964047.html and https://www.stats.gov.cn/english/PressRelease/202607/t20260710_1964093.html
- Fixed facts: The official manufacturing PMI was 50.3, up 0.3 point from May. Industrial producer prices increased 4.1% year over year and decreased 0.3% month over month.
- Source-reported status or uncertainty: A PMI above 50 denotes month-over-month expansion under the publisher's convention. Producer-price comparisons use the official index methodology.

### 12. Energy Data And Forecast

- Publisher: U.S. Energy Information Administration
- Publication dates: July 7 and July 15, 2026
- Observation periods: July Short-Term Energy Outlook and week ending July 10
- URLs: https://www.eia.gov/outlooks/steo/report/global_oil.php and https://www.eia.gov/petroleum/supply/weekly/
- Fixed facts: EIA reported that Brent crude averaged $85 per barrel in June and was below $70 on July 1. Its July forecast projected Brent averaging $103 in the second quarter and $70 in the fourth quarter of 2026. The latest Weekly Petroleum Status Report covered the week ending July 10 and was released July 15.
- Source-reported status or uncertainty: The Brent values beyond observed dates are EIA forecasts completed July 1 and can change. Weekly petroleum estimates are preliminary.

## Scheduled Catalysts Inside The Monthly Scoring Window

- July 17, 9:15 a.m. ET: Federal Reserve June industrial production and capacity utilization.
- July 22 and subsequent Wednesdays: EIA Weekly Petroleum Status Reports.
- July 28-29: Federal Reserve FOMC meeting; statement scheduled July 29.
- July 30, 8:30 a.m. ET: BEA advance second-quarter GDP and June personal income and outlays.
- July 30-31: Bank of Japan monetary policy meeting; statement and July outlook scheduled July 31, with timing not fixed on the July 10 BOJ calendar.
- August 7, 8:30 a.m. ET: BLS July Employment Situation.
- August 11: EIA August Short-Term Energy Outlook.
- August 12, 8:30 a.m. ET: BLS July CPI.
- August 13, 8:30 a.m. ET: BLS July PPI.
- August 14: the CapitalBench monthly exit snapshot uses the adjusted close after regular trading ends.

Calendar URLs: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm, https://www.bea.gov/news/schedule/full, https://www.bls.gov/schedule/2026/08_sched.htm, https://www.boj.or.jp/en/about/calendar/index.htm, and https://www.eia.gov/outlooks/steo/release_schedule.php.

## Prompt 1 Completion Check

- Facts stop at the research cutoff: yes.
- Primary public publishers used: yes.
- URLs, publication dates, observation dates, and reported uncertainty retained here: yes.
- Complete mechanical market artifact referenced without selecting winners: yes.
- Rankings, allocations, option recommendations, and affected-option mapping: none.
