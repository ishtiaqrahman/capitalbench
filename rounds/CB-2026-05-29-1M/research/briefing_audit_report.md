# Asset-Group Context For CapitalBench

## 1. Balanced Asset-Area Fact Ledger

| asset_area | covered_area | fact_type | balance_role | factual_statement | source_reported_comparison | comparison_type | date_or_period | source |
|---|---|---|---|---|---|---|---|---|
| cash and short-duration Treasuries | federal funds and short bills | policy_or_regulatory_fact | current_condition | The FOMC maintained the federal funds target range at 3.50% to 3.75%. | not source-reported | not source-reported | April 29, 2026 | Federal Reserve FOMC Statement - https://www.federalreserve.gov/monetarypolicy/files/monetary20260429a1.pdf |
| bonds and rates | Treasury curve | observed_value | current_condition | The 3-month, 2-year, 10-year, and 30-year Treasury constant maturity rates were 3.69%, 3.99%, 4.45%, and 4.98%, respectively. | not source-reported | not source-reported | May 28, 2026 | FRED Treasury Rates - https://fred.stlouisfed.org/series/DGS10 |
| bonds and rates | central-bank calendar | scheduled_event | scheduled_event | The next scheduled FOMC meeting is June 16-17, 2026. | not source-reported | not source-reported | June 16-17, 2026 | Federal Reserve FOMC Calendar - https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |
| credit | corporate credit | observed_value | current_condition | The ICE BofA US Corporate Index option-adjusted spread was 0.73%, and the ICE BofA US High Yield Index option-adjusted spread was 2.72%. | not source-reported | not source-reported | May 28, 2026 | FRED BAMLC0A0CM and BAMLH0A0HYM2 - https://fred.stlouisfed.org/series/BAMLC0A0CM |
| broad US equities | corporate profits | observed_value | current_condition | Profits from current production increased $40.4 billion in Q1 2026. | $246.9 billion increase in Q4 2025 | prior value | Q1 2026 second estimate | BEA GDP Second Estimate - https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-1st-quarter-2026 |
| broad US equities | real GDP | observed_value | counterbalancing_fact | Real GDP increased at a 1.6% annual rate in Q1 2026. | revised down 0.4 percentage point from the advance estimate; Q4 2025 was +0.5% | revision and prior value | Q1 2026 second estimate | BEA GDP Second Estimate - https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-1st-quarter-2026 |
| financials and regional banks | banking industry | observed_value | current_condition | FDIC-insured institutions reported a 1.26% return on assets ratio and $80.5 billion of aggregate net income. | net income increased $2.8 billion, or 3.6%, from the prior quarter | prior value | Q1 2026 | FDIC Quarterly Banking Profile - https://www.fdic.gov/quarterly-banking-profile |
| consumer sectors | consumer spending | observed_value | current_condition | Current-dollar personal consumption expenditures increased $111.1 billion, or 0.5%. | 1.0% in March 2026 | prior value | April 2026 | BEA Personal Income and Outlays - https://www.bea.gov/news/2026/personal-income-and-outlays-april-2026 |
| consumer sectors | consumer sentiment | observed_value | counterbalancing_fact | The University of Michigan Index of Consumer Sentiment was 44.8. | 49.8 in April 2026 and 52.2 in May 2025 | prior value and year-over-year change | May 2026 final | University of Michigan Surveys of Consumers - https://www.sca.isr.umich.edu/ |
| consumer sectors | retail sales calendar | scheduled_event | scheduled_event | Advance Monthly Sales for Retail and Food Services for May 2026 is scheduled for release on June 17, 2026. | not source-reported | not source-reported | June 17, 2026 | U.S. Census Monthly Retail Trade - https://www.census.gov/retail/sales.html |
| real estate | housing construction | observed_value | current_condition | Housing starts were 1,465,000 SAAR, and building permits were 1,442,000 SAAR. | starts down 2.8%; permits up 5.8% from March 2026 | month-over-month change | April 2026 | Census/HUD New Residential Construction - https://www.census.gov/construction/nrc/pdf/newresconst_202604.pdf |
| real estate | mortgage reference rates | observed_value | counterbalancing_fact | The 30-year fixed-rate mortgage average was 6.53%. | 6.51% previous week | prior value | week ending May 28, 2026 | FRED MORTGAGE30US - https://fred.stlouisfed.org/series/MORTGAGE30US |
| healthcare and biotechnology | prescription-drug policy | policy_or_regulatory_fact | current_condition | CMS published the selected-drug list and negotiated prices file for Medicare maximum fair prices. | not source-reported | not source-reported | May 26, 2026 | CMS Selected Drugs and Negotiated Prices - https://www.cms.gov/priorities/medicare-prescription-drug-affordability/overview/medicare-drug-price-negotiation-program/selected-drugs-negotiated-prices |
| software | software prices | observed_value | current_condition | The PCE Computer Software and Accessories category increased 13.9% year over year and roughly 73.1% annualized from November 2025 through March 2026. | average annualized rate of -5.3% over the prior 25 years | prior value | November 2025 through March 2026 | Federal Reserve FEDS Notes - https://www.federalreserve.gov/econres/notes/feds-notes/measurement-of-computer-software-and-accessories-inflation-20260522.html |
| semiconductors | global chip sales | observed_value | current_condition | Global semiconductor sales were $298.5 billion during Q1 2026. | up 25% compared to Q4 2025 | prior value | Q1 2026 | Semiconductor Industry Association - https://www.semiconductors.org/global-semiconductor-sales-increase-25-from-q4-2025-to-q1-2026/ |
| broad AI technology | AI spending | labeled_forecast_or_estimate | current_condition | Gartner forecast worldwide AI spending to total $2.59 trillion in 2026. | 47% increase year over year | year-over-year change | 2026 forecast, published May 2026 | Business Wire / Gartner - https://www.businesswire.com/news/home/20260519405832/en/Gartner-Forecasts-Worldwide-AI-Spending-to-Grow-47-in-2026 |
| AI infrastructure and utilities | AI capital expenditure and data-center electricity | labeled_forecast_or_estimate | current_condition | IEA reported capital expenditure of five large technology companies was more than $400 billion in 2025. | set to increase by a further 75% in 2026 | consensus / forecast comparison | 2025 and 2026 forecast, published April 16, 2026 | IEA Energy and AI - https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions |
| utilities | electricity demand | labeled_forecast_or_estimate | current_condition | EIA forecast U.S. electricity demand would rise 1.3% in 2026, average almost 4,250 billion kilowatthours, and grow another 3.1% in 2027. | not source-reported | not source-reported | May 2026 Short-Term Energy Outlook | EIA STEO - https://www.eia.gov/outlooks/steo/report/ |
| solar | utility-scale solar generation | labeled_forecast_or_estimate | current_condition | EIA said its utility-scale solar generation forecast for 2026 was 1.4% higher than in the previous STEO. | 1.4% higher than previous STEO | revision | May 2026 Short-Term Energy Outlook | EIA STEO - https://www.eia.gov/outlooks/steo/report/ |
| autonomous technology and robotics | North American robot orders | observed_value | current_condition | North American companies ordered 9,055 robots valued at $543 million in Q1 2026. | units decreased 0.1% and revenue declined 6.4% year over year | year-over-year change | Q1 2026 | Business Wire / Association for Advancing Automation - https://www.businesswire.com/news/home/20260511529781/en/Robot-Orders-Hold-Steady-in-Q1-2026-as-Demand-Broadens-Across-Non-Automotive-Industries |
| cybersecurity | AI cybersecurity spending | labeled_forecast_or_estimate | current_condition | Gartner listed AI cybersecurity spending of $85.997 billion in 2026 in its worldwide AI spending forecast. | $51.347 billion in 2025 | prior value | 2026 forecast, published May 2026 | Business Wire / Gartner - https://www.businesswire.com/news/home/20260519405832/en/Gartner-Forecasts-Worldwide-AI-Spending-to-Grow-47-in-2026 |
| aerospace and defense | U.S. defense budget request | policy_or_regulatory_fact | current_condition | The FY2027 U.S. defense budget request totaled $1.5 trillion, including a $1.15 trillion base request and $350 billion from reconciliation. | not source-reported | not source-reported | April 2026 | Breaking Defense - https://breakingdefense.com/2026/04/trump-to-propose-1-5-trillion-defense-budget-banking-on-350-billion-from-reconciliation/ |
| energy and oil | crude oil outlook | labeled_forecast_or_estimate | current_condition | EIA forecast global oil inventories would decrease by 2.6 million barrels per day in 2026. | last month's STEO forecast a 0.3 million barrel per day decrease | prior value | May 2026 Short-Term Energy Outlook | EIA STEO - https://www.eia.gov/outlooks/steo/report/ |
| energy and oil | OPEC supply policy | policy_or_regulatory_fact | counterbalancing_fact | Seven OPEC+ countries decided to implement a production adjustment of 188 thousand barrels per day from previous voluntary adjustments. | not source-reported | not source-reported | decision on May 3, 2026; adjustment for June 2026 | OPEC - https://www.opec.org/pr-detail/1779602-3-may-2026.html |
| broad commodities | commodity indexes | labeled_forecast_or_estimate | current_condition | The World Bank forecast overall commodity prices to increase 16% in 2026. | not source-reported | not source-reported | April 2026 Commodity Markets Outlook | World Bank Commodity Markets Outlook - https://www.worldbank.org/en/news/press-release/2026/04/28/commodity-markets-outlook-april-2026-press-release |
| precious metals | gold and silver | labeled_forecast_or_estimate | current_condition | The World Bank forecast average precious-metals prices to increase 42% in 2026. | not source-reported | not source-reported | April 2026 Commodity Markets Outlook | World Bank Commodity Markets Outlook - https://www.worldbank.org/en/news/press-release/2026/04/28/commodity-markets-outlook-april-2026-press-release |
| metals and mining | base metals and copper | labeled_forecast_or_estimate | current_condition | The World Bank said average base-metals prices were projected to reach all-time highs. | not source-reported | not source-reported | April 2026 Commodity Markets Outlook | World Bank Commodity Markets Outlook - https://www.worldbank.org/en/news/press-release/2026/04/28/commodity-markets-outlook-april-2026-press-release |
| agriculture | grains and oilseeds | labeled_forecast_or_estimate | current_condition | USDA forecast the U.S. corn crop at 16.0 billion bushels for 2026/27. | down 6% from a year ago | year-over-year change | 2026/27 marketing year forecast, May 2026 WASDE | USDA WASDE - https://esmis.nal.usda.gov/sites/default/release-files/795903/wasde0526v2.pdf |
| currencies | U.S. dollar, euro, and yen | observed_value | current_condition | U.S. Dollar Index futures, EUR/USD, and USD/JPY were quoted at 98.890, 1.16646, and 159.2635, respectively. | not source-reported | not source-reported | May 29, 2026 | Stooq Currency Quotes - https://stooq.com/q/l/?s=dx.f,eurusd,usdjpy&f=sd2t2ohlcvn&h&e=csv |
| crypto proxies | bitcoin and ethereum | observed_value | current_condition | Bitcoin and ethereum were quoted at 73,346.17 and 2,008.484, respectively. | not source-reported | not source-reported | May 30, 2026 source time | Stooq Crypto Quotes - https://stooq.com/q/l/?s=btc.v,eth.v&f=sd2t2ohlcvn&h&e=csv |
| Europe equities | euro area policy | policy_or_regulatory_fact | current_condition | The ECB held the deposit facility, main refinancing operations, and marginal lending facility rates at 2.00%, 2.15%, and 2.40%, respectively. | not source-reported | not source-reported | April 30, 2026 | European Central Bank - https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260430~81b7179e6f.en.html |
| Japan equities | Japan policy rate | policy_or_regulatory_fact | current_condition | The Bank of Japan encouraged the uncollateralized overnight call rate to remain at around 0.75%. | not source-reported | not source-reported | April 28, 2026 | Bank of Japan Monetary Policy Statement - https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260428a.pdf |
| China equities | credit policy and manufacturing survey | policy_or_regulatory_fact | current_condition | China's one-year Loan Prime Rate was 3.0%, and its five-year Loan Prime Rate was 3.5%; China's official manufacturing PMI was 50.3 in April 2026. | manufacturing PMI down 0.1 percentage point from the previous month | month-over-month change | May 2026 LPR; April 2026 PMI | Trading Economics China Interest Rate - https://tradingeconomics.com/china/interest-rate ; National Bureau of Statistics of China PMI - https://www.stats.gov.cn/english/PressRelease/202605/t20260506_1963595.html |
| India equities | inflation and monetary policy | observed_value | current_condition | India's April 2026 CPI inflation was 3.48%, and the Reserve Bank of India policy repo rate was 5.25%. | CPI was 3.40% in March 2026 | prior value | April 2026 CPI; April 2026 monetary policy | Press Information Bureau India CPI - https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260251 ; Reserve Bank of India Current Rates - https://m.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=20936 |

## 2. Asset-Area Tension Ledger

| asset_area | source_reported_fact_1 | source_reported_fact_2 | unresolved_question | source_or_sources |
|---|---|---|---|---|
| bonds and rates | The 10-year Treasury constant maturity rate was 4.45% on May 28, 2026. | The next scheduled FOMC meeting is June 16-17, 2026. | June 2026 FOMC policy decision | FRED DGS10 - https://fred.stlouisfed.org/series/DGS10 ; Federal Reserve FOMC Calendar - https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |
| broad US equities | Profits from current production increased $40.4 billion in Q1 2026. | Real GDP increased at a 1.6% annual rate in Q1 2026 and was revised down 0.4 percentage point from the advance estimate. | Q1 2026 third GDP and corporate-profits estimate | BEA GDP Second Estimate - https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-1st-quarter-2026 |
| consumer sectors | Current-dollar personal consumption expenditures increased 0.5% in April 2026. | University of Michigan Index of Consumer Sentiment was 44.8 in May 2026 final results. | May 2026 retail sales release | BEA Personal Income and Outlays - https://www.bea.gov/news/2026/personal-income-and-outlays-april-2026 ; University of Michigan Surveys of Consumers - https://www.sca.isr.umich.edu/ |
| real estate | Housing starts were 1,465,000 SAAR in April 2026. | The 30-year fixed-rate mortgage average was 6.53% for the week ending May 28, 2026. | May 2026 housing starts, building permits, and existing-home sales releases | Census/HUD New Residential Construction - https://www.census.gov/construction/nrc/pdf/newresconst_202604.pdf ; FRED MORTGAGE30US - https://fred.stlouisfed.org/series/MORTGAGE30US |
| semiconductors and software | Global semiconductor sales were $298.5 billion during Q1 2026. | The PCE Computer Software and Accessories category increased roughly 73.1% annualized from November 2025 through March 2026. | Next SIA monthly semiconductor sales release and May 2026 PCE software readings | Semiconductor Industry Association - https://www.semiconductors.org/global-semiconductor-sales-increase-25-from-q4-2025-to-q1-2026/ ; Federal Reserve FEDS Notes - https://www.federalreserve.gov/econres/notes/feds-notes/measurement-of-computer-software-and-accessories-inflation-20260522.html |
| energy and commodities | EIA forecast global oil inventories would decrease by 2.6 million barrels per day in 2026. | Seven OPEC+ countries decided on a 188 thousand barrel per day production adjustment for June 2026. | June 2026 OPEC+ review meeting and June 2026 EIA STEO release | EIA STEO - https://www.eia.gov/outlooks/steo/report/ ; OPEC - https://www.opec.org/pr-detail/1779602-3-may-2026.html |
| international equities | The ECB held its three key rates at 2.00%, 2.15%, and 2.40%. | The Bank of Japan encouraged the uncollateralized overnight call rate to remain at around 0.75%. | June 2026 ECB and BOJ monetary policy decisions | European Central Bank - https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260430~81b7179e6f.en.html ; Bank of Japan - https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260428a.pdf |
| AI infrastructure and utilities | IEA reported capital expenditure of five large technology companies was more than $400 billion in 2025. | EIA forecast U.S. electricity demand would rise 1.3% in 2026 and 3.1% in 2027. | Next EIA electricity-demand forecast update | IEA Energy and AI - https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions ; EIA STEO - https://www.eia.gov/outlooks/steo/report/ |

## 3. Scheduled Asset-Area Events

| date | asset_area | event | entity_or_publisher | source |
|---|---|---|---|---|
| June 1 and June 3, 2026 10:00 AM ET | industrials; materials; consumer sectors; broad US equities | ISM Manufacturing PMI and ISM Services PMI, May 2026 | Institute for Supply Management | ISM Report Calendar - https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/ |
| June 5, 2026 8:30 AM ET | bonds and rates; broad US equities | Employment Situation, May 2026 | U.S. Bureau of Labor Statistics | BLS Employment Situation - https://www.bls.gov/news.release/empsit.htm |
| June 9, 2026 | energy and oil; broad commodities | Short-Term Energy Outlook next release | U.S. Energy Information Administration | EIA STEO - https://www.eia.gov/outlooks/steo/report/ |
| June 10 and June 11, 2026 8:30 AM ET | bonds and rates; TIPS; broad US equities; materials | CPI and Producer Price Index, May 2026 | U.S. Bureau of Labor Statistics | BLS Release Calendar - https://www.bls.gov/schedule/news_release/ |
| June 10, 2026 | Canada equities; Canadian dollar | Interest rate announcement | Bank of Canada | Bank of Canada Policy Interest Rate - https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/ |
| June 11, 2026 | Europe equities; euro | ECB Governing Council monetary policy meeting | European Central Bank | ECB Governing Council Calendar - https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html |
| June 16 and June 17, 2026 | real estate; consumer sectors | New Residential Construction and Advance Monthly Retail Sales, May 2026 | U.S. Census Bureau and HUD | Census/HUD New Residential Construction - https://www.census.gov/construction/nrc/ |
| June 16-17, 2026 | bonds and rates; U.S. dollar; broad US equities | FOMC meeting | Federal Reserve | Federal Reserve FOMC Calendar - https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |
| June 16-17, 2026 | Japan equities; yen | Monetary Policy Meeting | Bank of Japan | Bank of Japan MPM Schedule - https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm |
| June 18, 2026 | UK equities; sterling | Monetary Policy Committee decision | Bank of England | Bank of England MPC Dates - https://www.bankofengland.co.uk/monetary-policy/upcoming-mpc-dates |
| June 22, 2026 | China equities; renminbi | China Loan Prime Rate fixing | People's Bank of China / National Interbank Funding Center | Trading Economics China Interest Rate Calendar - https://tradingeconomics.com/china/interest-rate |
| June 25, 2026 8:30 AM ET | consumer sectors; bonds and rates; broad US equities | Personal Income and Outlays, May 2026; GDP third estimate, Q1 2026 | U.S. Bureau of Economic Analysis | BEA Release Schedule - https://www.bea.gov/news/schedule |

## 4. Coverage And Bias Audit

| asset_area | rows_in_fact_ledger | current_condition_rows | counterbalancing_or_uncertainty_rows | scheduled_event_rows | note |
|---|---:|---:|---:|---:|---|
| cash and short-duration Treasuries | 1 | 1 | 0 | 0 | only one cited current row used |
| bonds and rates | 2 | 1 | 0 | 1 | scheduled FOMC row included |
| credit | 1 | 1 | 0 | 0 | only one cited current row used |
| broad US equities | 2 | 1 | 1 | 0 | GDP revision row included |
| financials and regional banks | 1 | 1 | 0 | 0 | only one cited current row used |
| consumer sectors | 3 | 1 | 1 | 1 | reached one-month row cap |
| real estate | 2 | 1 | 1 | 0 | mortgage-rate row included |
| healthcare and biotechnology | 1 | 1 | 0 | 0 | only one policy row used |
| software | 1 | 1 | 0 | 0 | only one cited current row used |
| semiconductors | 1 | 1 | 0 | 0 | row cap not reached |
| broad AI technology | 1 | 1 | 0 | 0 | one broad spending forecast used |
| AI infrastructure and utilities | 1 | 1 | 0 | 0 | one broad infrastructure forecast used |
| utilities | 1 | 1 | 0 | 0 | one electricity-demand forecast used |
| solar | 1 | 1 | 0 | 0 | one utility-scale solar forecast row used |
| autonomous technology and robotics | 1 | 1 | 0 | 0 | one industry order row used |
| cybersecurity | 1 | 1 | 0 | 0 | one broad AI cybersecurity spending row used |
| aerospace and defense | 1 | 1 | 0 | 0 | one policy row used |
| energy and oil | 2 | 1 | 1 | 0 | OPEC policy row included |
| broad commodities | 1 | 1 | 0 | 0 | one commodity forecast row used |
| precious metals | 1 | 1 | 0 | 0 | one precious-metals forecast row used |
| metals and mining | 1 | 1 | 0 | 0 | one base-metals forecast row used |
| agriculture | 1 | 1 | 0 | 0 | one USDA forecast row used |
| currencies | 1 | 1 | 0 | 0 | one current quote row used |
| crypto proxies | 1 | 1 | 0 | 0 | one current quote row used |
| Europe equities | 1 | 1 | 0 | 0 | one policy row used |
| Japan equities | 1 | 1 | 0 | 0 | one policy row used |
| China equities | 1 | 1 | 0 | 0 | one policy and survey row used |
| India equities | 1 | 1 | 0 | 0 | one inflation and policy row used |

## 5. Skipped Groups

| asset_area | reason_skipped |
|---|---|
| value, size, dividend, low-volatility, and momentum factors | duplicate of mechanical return table |
| communication services | too single-company-specific |
| consumer discretionary and consumer staples as separate rows | no material recent fact found |
| materials excluding metals and mining | duplicate of mechanical return table |
| aggregate bonds as a separate row | duplicate of mechanical return table |
| mortgage-backed bonds as a separate row | duplicate of mechanical return table |
| municipal bonds | no material recent fact found |
| emerging-market bonds | no material recent fact found |
| international aggregate bonds | no material recent fact found |
| developed ex-US aggregate | duplicate of mechanical return table |
| Australia equities | no material recent fact found |
| South Korea equities | too single-company-specific |
| Taiwan equities | too single-company-specific |
| Brazil equities | no material recent fact found |
| Mexico equities | no material recent fact found |
| South Africa equities | no material recent fact found |
