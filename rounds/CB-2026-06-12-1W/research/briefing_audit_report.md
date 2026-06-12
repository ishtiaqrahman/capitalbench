# Asset-Area Datapoint Matrix For CapitalBench

## 1. Research Setup

| field | value |
| --- | --- |
| decision_deadline | 2026-06-12T23:30:00Z |
| round_horizon | ONE WEEK |
| exit_date | 2026-06-19 |
| source_collection_rule | latest available information at research run time |

## 2. Fixed Asset-Area Datapoints

| row_id | asset_area | requested_datapoint | latest_value_or_fact | unit_if_applicable | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH_SHORT_TREASURY_POLICY_RATE | cash and short-duration Treasuries | current federal funds target range or nearest official short-rate policy setting | Federal funds target range 3.50-3.75 percent | percent | not source-reported | not source-reported | since 2026-04-29 | 2026-04-29 | Federal Reserve FOMC Statement - https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm | policy_or_regulatory_fact |
| BROAD_US_EQUITIES_CORPORATE_PROFITS | broad US equities | latest official corporate profits or broad index earnings aggregate | Profits from current production increased $40.4 billion in Q1 2026 | USD | increase of $246.9 billion in Q4 2025 | prior value | Q1 2026 | 2026-05-28 | BEA GDP Second Estimate and Corporate Profits - https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-1st-quarter-2026 | observed |
| BROAD_US_EQUITIES_GDP | broad US equities | latest real GDP growth value | Real GDP increased at a 1.6 percent annualized rate in Q1 2026 | percent | 0.5 percent in Q4 2025 | prior value | Q1 2026 | 2026-05-28 | BEA GDP Second Estimate and Corporate Profits - https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-1st-quarter-2026 | observed |
| BROAD_US_EQUITIES_VALUATION | broad US equities | latest broad valuation datapoint such as forward P/E, CAPE, or earnings yield if source-reported | S&P 500 forward 12-month P/E ratio 21.1 | ratio | 19.7 at 2026-03-31 | prior value | June 2026 report | 2026-06-06 | FactSet Earnings Insight - https://www.factset.com/earningsinsight | observed |
| BROAD_US_EQUITIES_MARKET_BREADTH | broad US equities | latest broad market breadth datapoint if source-reported | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| NASDAQ_GROWTH_TECH_INDEX_OR_SECTOR_FACT | Nasdaq / growth / technology | latest broad technology sector or Nasdaq-level fact, not single-company news | NASDAQ Composite closed at 25,809.660 on 2026-06-11 | index | 25,169.500 on 2026-06-10 | prior value | 2026-06-11 close | 2026-06-11 | FRED NASDAQ Composite - https://fred.stlouisfed.org/series/NASDAQCOM | observed |
| LARGE_GROWTH_CONTEXT | large-cap growth | latest broad large-growth style fact, valuation fact, earnings fact, or factor fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| LARGE_VALUE_CONTEXT | large-cap value | latest broad large-value style fact, valuation fact, earnings fact, or factor fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| MID_CAP_CONTEXT | mid-cap equities | latest broad mid-cap index, earnings, financing, or domestic-growth fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| SMALL_CAP_CONTEXT | small-cap equities | latest broad small-cap index, earnings, financing, or domestic-growth fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| SMALL_VALUE_CONTEXT | small-cap value | latest broad small-value style, valuation, earnings, or financing fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| DIVIDEND_CONTEXT | dividend equities | latest broad dividend-yield, payout, dividend-growth, or factor fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| LOW_VOLATILITY_CONTEXT | low-volatility equities | latest broad low-volatility factor, realized volatility, low-beta factor, or minimum-volatility factor fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| MOMENTUM_CONTEXT | momentum equities | latest broad momentum factor, factor rotation, or style-index fact from a reliable source | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| COMMUNICATION_SERVICES_CONTEXT | communication services | latest broad sector fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| CONSUMER_DISCRETIONARY_CONTEXT | consumer discretionary | latest broad sector fact or consumer spending datapoint | Retail and food services sales increased 0.5 percent month over month in April 2026 | percent | 1.6 percent in March 2026 | prior value | Apr 2026 | 2026-05-14 | U.S. Census Monthly Retail Trade - https://www.census.gov/retail/sales.html | observed |
| CONSUMER_STAPLES_CONTEXT | consumer staples | latest broad sector fact or consumer spending/inflation datapoint | Food at home CPI increased 0.1 percent month over month and 2.7 percent year over year in May 2026 | percent | not source-reported | not source-reported | May 2026 | 2026-06-10 | BLS CPI News Release - https://www.bls.gov/news.release/cpi.nr0.htm | observed |
| HEALTHCARE_CONTEXT | healthcare | latest broad sector, policy, or spending fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| BIOTECH_CONTEXT | biotechnology | latest broad biotech industry, policy, or index-level fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| FINANCIALS_CONTEXT | financials | latest broad banking, credit, or financial-sector fact | Money market fund assets were $7.87 trillion for the week ended 2026-06-10 | USD | decreased by $21.48 billion | week-over-week change | week ended 2026-06-10 | 2026-06-11 | Investment Company Institute Money Market Fund Assets - https://www.ici.org/research/stats/mmf | observed |
| REGIONAL_BANKS_CONTEXT | regional banks | latest regional-bank industry, FDIC, credit, or deposit fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| INDUSTRIALS_CONTEXT | industrials | latest industrial production, manufacturing, or broad sector fact | Industrial production increased 0.7 percent in April 2026 | percent | -0.3 percent in March 2026 | prior value | Apr 2026 | 2026-05-15 | Federal Reserve G.17 - https://www.federalreserve.gov/releases/g17/current/default.htm | observed |
| AEROSPACE_DEFENSE_CONTEXT | aerospace and defense | latest broad defense budget, orders, production, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| ENERGY_CONTEXT | energy | latest broad energy-sector, oil/gas supply, or inventory fact | WTI crude oil spot price was $95.00 per barrel on 2026-06-08 | USD/barrel | $94.32 on 2026-06-05 | prior value | 2026-06-08 | 2026-06-10 | FRED WTI Crude Oil - https://fred.stlouisfed.org/series/DCOILWTICO | observed |
| MATERIALS_CONTEXT | materials | latest broad materials, chemicals, or industrial-input fact | Producer Price Index final demand goods increased 2.8 percent in May 2026 | percent | not source-reported | not source-reported | May 2026 | 2026-06-11 | BLS PPI News Release - https://www.bls.gov/news.release/ppi.nr0.htm | observed |
| METALS_MINING_CONTEXT | metals and mining | latest broad metals/mining production, price, inventory, or forecast fact | Global copper price was $13,483.75154 per metric ton in May 2026 | USD/metric ton | $12,890.68773 in April 2026 | prior value | May 2026 | 2026-06-05 | FRED Global Copper Price - https://fred.stlouisfed.org/series/PCOPPUSDM | observed |
| UTILITIES_CONTEXT | utilities | latest electricity demand, generation, rate, or broad utility-sector fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| REAL_ESTATE_CONTEXT | real estate | latest housing, REIT, mortgage, or property-market fact | Existing-home sales were 4.17 million at a seasonally adjusted annual rate in May 2026 | million units | 3.2 percent above April 2026 | month-over-month change | May 2026 | 2026-06-09 | National Association of Realtors Existing-Home Sales - https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales | observed |
| INTERMEDIATE_TREASURY_CONTEXT | intermediate Treasuries | latest Treasury yield or policy fact from macro packet if no separate broad source exists | 5-year Treasury constant maturity yield was 4.27 percent on 2026-06-10 | percent | 4.26 percent on 2026-06-09 | prior value | 2026-06-10 | 2026-06-11 | Federal Reserve H.15 Selected Interest Rates - https://www.federalreserve.gov/releases/h15/ | observed |
| LONG_TREASURY_CONTEXT | long Treasuries | latest long-term Treasury yield or policy fact from macro packet if no separate broad source exists | 30-year Treasury constant maturity yield was 5.03 percent on 2026-06-10 | percent | 5.01 percent on 2026-06-09 | prior value | 2026-06-10 | 2026-06-11 | Federal Reserve H.15 Selected Interest Rates - https://www.federalreserve.gov/releases/h15/ | observed |
| TIPS_CONTEXT | TIPS | latest real yield or inflation-expectation fact | 10-year TIPS constant maturity yield was 2.21 percent on 2026-06-10 | percent | 2.20 percent on 2026-06-09 | prior value | 2026-06-10 | 2026-06-11 | Federal Reserve H.15 Selected Interest Rates - https://www.federalreserve.gov/releases/h15/ | observed |
| AGGREGATE_BONDS_CONTEXT | aggregate bonds | latest aggregate bond-market yield, duration, or broad fixed-income fact | 10-year Treasury constant maturity yield was 4.55 percent on 2026-06-10 | percent | 4.53 percent on 2026-06-09 | prior value | 2026-06-10 | 2026-06-11 | Federal Reserve H.15 Selected Interest Rates - https://www.federalreserve.gov/releases/h15/ | observed |
| MBS_CONTEXT | agency mortgage-backed bonds | latest mortgage-rate or agency MBS market fact | 30-year fixed-rate mortgage averaged 6.52 percent for the week of 2026-06-11 | percent | 6.48 percent prior week; 6.84 percent one year ago | prior value and year-over-year comparison | week of 2026-06-11 | 2026-06-11 | Freddie Mac PMMS - https://www.freddiemac.com/pmms | observed |
| MUNICIPAL_BONDS_CONTEXT | municipal bonds | latest municipal bond yield, issuance, credit, or fund-flow fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| INVESTMENT_GRADE_CREDIT_CONTEXT | investment-grade credit | latest investment-grade credit spread or broad corporate credit fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| HIGH_YIELD_CREDIT_CONTEXT | high-yield credit | latest high-yield credit spread or default/fund-flow fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| EMERGING_MARKET_BONDS_CONTEXT | emerging-market bonds | latest EM bond spread, yield, flow, or debt fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| INTERNATIONAL_BONDS_CONTEXT | international aggregate bonds | latest non-US aggregate bond yield, hedged global bond, currency-hedging, or international rates fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| DEVELOPED_EX_US_CONTEXT | developed ex-US equities | latest developed-market ex-US or MSCI/EAFE-level fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| EMERGING_MARKETS_CONTEXT | emerging-market equities | latest broad emerging-market equity, GDP, PMI, flows, currency, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| EUROPE_CONTEXT | Europe equities | latest ECB, euro area GDP, inflation, PMI, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| JAPAN_CONTEXT | Japan equities | latest BOJ, Japan GDP, inflation, PMI, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| CHINA_CONTEXT | China equities | latest China GDP, PMI, LPR, inflation, trade, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| INDIA_CONTEXT | India equities | latest India GDP, CPI, RBI, PMI, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| CANADA_CONTEXT | Canada equities | latest Bank of Canada, GDP, CPI, commodity, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| UK_CONTEXT | UK equities | latest Bank of England, GDP, CPI, PMI, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| AUSTRALIA_CONTEXT | Australia equities | latest RBA, GDP, CPI, commodity, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| SOUTH_KOREA_CONTEXT | South Korea equities | latest Korea GDP, exports, CPI, Bank of Korea, semiconductor export, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| TAIWAN_CONTEXT | Taiwan equities | latest Taiwan GDP, exports, inflation, central-bank, semiconductor export, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| BRAZIL_CONTEXT | Brazil equities | latest Brazil GDP, inflation, central-bank, commodity, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| MEXICO_CONTEXT | Mexico equities | latest Mexico GDP, inflation, central-bank, trade, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| SOUTH_AFRICA_CONTEXT | South Africa equities | latest South Africa GDP, inflation, central-bank, commodity, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| GOLD_CONTEXT | gold | latest broad gold price, demand, central-bank purchases, or forecast fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| SILVER_CONTEXT | silver | latest broad silver price, demand, supply, or forecast fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| COPPER_CONTEXT | copper | latest broad copper price, inventory, demand, supply, or forecast fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| AGRICULTURE_CONTEXT | agriculture | latest broad agriculture price, crop, WASDE, or supply fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| BROAD_COMMODITIES_CONTEXT | broad commodities | latest broad commodity index, World Bank, or commodity-market fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| OIL_CONTEXT | oil | latest oil price, inventory, OPEC, EIA, supply, or demand fact | Brent crude oil spot price was $97.46 per barrel on 2026-06-08 | USD/barrel | $97.29 on 2026-06-05 | prior value | 2026-06-08 | 2026-06-10 | FRED Brent Crude Oil - https://fred.stlouisfed.org/series/DCOILBRENTEU | observed |
| US_DOLLAR_CONTEXT | US dollar | latest DXY or broad dollar fact | Nominal Broad U.S. Dollar Index was 120.0831 on 2026-06-05 | index | 119.3615 on 2026-06-04 | prior value | 2026-06-05 | 2026-06-08 | FRED Nominal Broad U.S. Dollar Index - https://fred.stlouisfed.org/series/DTWEXBGS | observed |
| EURO_CONTEXT | euro | latest ECB, EUR/USD, euro-area rate, or currency fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| YEN_CONTEXT | yen | latest BOJ, USD/JPY, Japan rate, or currency fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| BITCOIN_CONTEXT | bitcoin proxy | latest bitcoin price, ETF flow, regulatory, or market-structure fact | Coinbase Bitcoin price was $63,482.72 on 2026-06-11 | USD | $61,570.02 on 2026-06-10 | prior value | 2026-06-11 | 2026-06-11 | FRED Coinbase Bitcoin - https://fred.stlouisfed.org/series/CBBTCUSD | observed |
| ETHEREUM_CONTEXT | ethereum proxy | latest ethereum price, ETF flow, regulatory, or market-structure fact | Coinbase Ethereum price was $1,668.89 on 2026-06-11 | USD | $1,622.27 on 2026-06-10 | prior value | 2026-06-11 | 2026-06-11 | FRED Coinbase Ethereum - https://fred.stlouisfed.org/series/CBETHUSD | observed |
| SEMICONDUCTORS_CONTEXT | semiconductors | latest global semiconductor sales, industry shipment, equipment, export, or broad supply-chain fact | NASDAQ Composite closed at 25,809.660 on 2026-06-11 | index | 25,169.500 on 2026-06-10 | prior value | 2026-06-11 close | 2026-06-11 | FRED NASDAQ Composite - https://fred.stlouisfed.org/series/NASDAQCOM | observed |
| SOFTWARE_CONTEXT | software | latest broad software price, spending, revenue, or sector fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| BROAD_AI_TECH_CONTEXT | broad AI technology | latest broad AI spending, investment, infrastructure, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| AUTONOMOUS_ROBOTICS_CONTEXT | autonomous technology / robotics | latest robotics order, automation, industrial robot, or policy fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| CYBERSECURITY_CONTEXT | cybersecurity | latest broad cybersecurity spending, incident count, policy, or sector fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |
| AI_INFRASTRUCTURE_CONTEXT | AI infrastructure | latest data-center, power demand, capex, chips, cloud infrastructure, or policy fact | S&P 500 CY 2026 earnings growth estimate was 22.8 percent in FactSet Earnings Insight | percent | not source-reported | not source-reported | June 2026 report | 2026-06-06 | FactSet Earnings Insight - https://www.factset.com/earningsinsight | forecast_or_estimate |
| SOLAR_CONTEXT | solar | latest solar generation, installation, capacity, policy, or forecast fact | not provided |  | not provided | not provided | not provided | not provided | not provided | not_provided |

## 3. Scheduled Asset-Area Events

| event_id | date | asset_area | event | entity_or_publisher | source | status |
| --- | --- | --- | --- | --- | --- | --- |
| NEXT_MAJOR_CENTRAL_BANK_EVENTS | 2026-06-14 to 2026-06-18 | cash and short-duration Treasuries; bonds and rates; international equities | BOJ Monetary Policy Meeting; FOMC decision; BOE MPC summary and minutes | Bank of Japan; Federal Reserve; Bank of England | Federal Reserve FOMC Calendar - https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm; Bank of Japan Monetary Policy Meetings - https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm; Bank of England MPC Dates - https://www.bankofengland.co.uk/monetary-policy/upcoming-mpc-dates | scheduled |
| NEXT_MAJOR_COUNTRY_INFLATION_RELEASES | not scheduled inside scoring window | broad US equities; bonds and rates; TIPS; consumer sectors | not scheduled inside scoring window | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_COUNTRY_GDP_RELEASES | not scheduled inside scoring window | broad US equities | not scheduled inside scoring window | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_COUNTRY_PMI_RELEASES | not scheduled inside scoring window | broad US equities; industrials | not scheduled inside scoring window | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_COMMODITY_POLICY_OR_INVENTORY_EVENTS | 2026-06-17 | energy; oil; agriculture | EIA Weekly Petroleum Status Report | U.S. Energy Information Administration | EIA Weekly Petroleum Status Report - https://www.eia.gov/petroleum/supply/weekly/ | scheduled |
| NEXT_MAJOR_ENERGY_REPORTS | 2026-06-17 | energy; oil | Weekly Petroleum Status Report | U.S. Energy Information Administration | EIA Weekly Petroleum Status Report - https://www.eia.gov/petroleum/supply/weekly/ | scheduled |
| NEXT_MAJOR_TREASURY_OR_CREDIT_EVENTS | 2026-06-16 to 2026-06-18 | intermediate and long Treasuries; TIPS | 20-year bond reopening and 5-year TIPS reopening auctions | U.S. Treasury | U.S. Treasury Tentative Auction Schedule - https://home.treasury.gov/system/files/221/Tentative-Auction-Schedule.pdf | scheduled |
| NEXT_MAJOR_BROAD_INDEX_EARNINGS_MILESTONE | not scheduled inside scoring window | broad US equities | not scheduled inside scoring window | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_SECTOR_POLICY_EVENTS | not scheduled inside scoring window | healthcare; sector policy | not scheduled inside scoring window | not provided | not provided | not_scheduled_inside_window |
| NEXT_MAJOR_CRYPTO_REGULATORY_OR_ETF_EVENTS | not scheduled inside scoring window | bitcoin proxy; ethereum proxy | not scheduled inside scoring window | not provided | not provided | not_scheduled_inside_window |

## 4. Missing Asset-Area Datapoints

| section | row_or_event_id | asset_area | missing_or_limited_item | note |
| --- | --- | --- | --- | --- |
| Section 2 | BROAD_US_EQUITIES_MARKET_BREADTH | broad US equities | latest broad market breadth datapoint if source-reported | not provided in source reports |
| Section 2 | LARGE_GROWTH_CONTEXT | large-cap growth | latest broad large-growth style fact, valuation fact, earnings fact, or factor fact | not provided in source reports |
| Section 2 | LARGE_VALUE_CONTEXT | large-cap value | latest broad large-value style fact, valuation fact, earnings fact, or factor fact | not provided in source reports |
| Section 2 | MID_CAP_CONTEXT | mid-cap equities | latest broad mid-cap index, earnings, financing, or domestic-growth fact | not provided in source reports |
| Section 2 | SMALL_CAP_CONTEXT | small-cap equities | latest broad small-cap index, earnings, financing, or domestic-growth fact | not provided in source reports |
| Section 2 | SMALL_VALUE_CONTEXT | small-cap value | latest broad small-value style, valuation, earnings, or financing fact | not provided in source reports |
| Section 2 | DIVIDEND_CONTEXT | dividend equities | latest broad dividend-yield, payout, dividend-growth, or factor fact | not provided in source reports |
| Section 2 | LOW_VOLATILITY_CONTEXT | low-volatility equities | latest broad low-volatility factor, realized volatility, low-beta factor, or minimum-volatility factor fact | not provided in source reports |
| Section 2 | MOMENTUM_CONTEXT | momentum equities | latest broad momentum factor, factor rotation, or style-index fact from a reliable source | not provided in source reports |
| Section 2 | COMMUNICATION_SERVICES_CONTEXT | communication services | latest broad sector fact | not provided in source reports |
| Section 2 | HEALTHCARE_CONTEXT | healthcare | latest broad sector, policy, or spending fact | not provided in source reports |
| Section 2 | BIOTECH_CONTEXT | biotechnology | latest broad biotech industry, policy, or index-level fact | not provided in source reports |
| Section 2 | REGIONAL_BANKS_CONTEXT | regional banks | latest regional-bank industry, FDIC, credit, or deposit fact | not provided in source reports |
| Section 2 | AEROSPACE_DEFENSE_CONTEXT | aerospace and defense | latest broad defense budget, orders, production, or policy fact | not provided in source reports |
| Section 2 | UTILITIES_CONTEXT | utilities | latest electricity demand, generation, rate, or broad utility-sector fact | not provided in source reports |
| Section 2 | MUNICIPAL_BONDS_CONTEXT | municipal bonds | latest municipal bond yield, issuance, credit, or fund-flow fact | not provided in source reports |
| Section 2 | INVESTMENT_GRADE_CREDIT_CONTEXT | investment-grade credit | latest investment-grade credit spread or broad corporate credit fact | not provided in source reports |
| Section 2 | HIGH_YIELD_CREDIT_CONTEXT | high-yield credit | latest high-yield credit spread or default/fund-flow fact | not provided in source reports |
| Section 2 | EMERGING_MARKET_BONDS_CONTEXT | emerging-market bonds | latest EM bond spread, yield, flow, or debt fact | not provided in source reports |
| Section 2 | INTERNATIONAL_BONDS_CONTEXT | international aggregate bonds | latest non-US aggregate bond yield, hedged global bond, currency-hedging, or international rates fact | not provided in source reports |
| Section 2 | DEVELOPED_EX_US_CONTEXT | developed ex-US equities | latest developed-market ex-US or MSCI/EAFE-level fact | not provided in source reports |
| Section 2 | EMERGING_MARKETS_CONTEXT | emerging-market equities | latest broad emerging-market equity, GDP, PMI, flows, currency, or policy fact | not provided in source reports |
| Section 2 | EUROPE_CONTEXT | Europe equities | latest ECB, euro area GDP, inflation, PMI, or policy fact | not provided in source reports |
| Section 2 | JAPAN_CONTEXT | Japan equities | latest BOJ, Japan GDP, inflation, PMI, or policy fact | not provided in source reports |
| Section 2 | CHINA_CONTEXT | China equities | latest China GDP, PMI, LPR, inflation, trade, or policy fact | not provided in source reports |
| Section 2 | INDIA_CONTEXT | India equities | latest India GDP, CPI, RBI, PMI, or policy fact | not provided in source reports |
| Section 2 | CANADA_CONTEXT | Canada equities | latest Bank of Canada, GDP, CPI, commodity, or policy fact | not provided in source reports |
| Section 2 | UK_CONTEXT | UK equities | latest Bank of England, GDP, CPI, PMI, or policy fact | not provided in source reports |
| Section 2 | AUSTRALIA_CONTEXT | Australia equities | latest RBA, GDP, CPI, commodity, or policy fact | not provided in source reports |
| Section 2 | SOUTH_KOREA_CONTEXT | South Korea equities | latest Korea GDP, exports, CPI, Bank of Korea, semiconductor export, or policy fact | not provided in source reports |
| Section 2 | TAIWAN_CONTEXT | Taiwan equities | latest Taiwan GDP, exports, inflation, central-bank, semiconductor export, or policy fact | not provided in source reports |
| Section 2 | BRAZIL_CONTEXT | Brazil equities | latest Brazil GDP, inflation, central-bank, commodity, or policy fact | not provided in source reports |
| Section 2 | MEXICO_CONTEXT | Mexico equities | latest Mexico GDP, inflation, central-bank, trade, or policy fact | not provided in source reports |
| Section 2 | SOUTH_AFRICA_CONTEXT | South Africa equities | latest South Africa GDP, inflation, central-bank, commodity, or policy fact | not provided in source reports |
| Section 2 | GOLD_CONTEXT | gold | latest broad gold price, demand, central-bank purchases, or forecast fact | not provided in source reports |
| Section 2 | SILVER_CONTEXT | silver | latest broad silver price, demand, supply, or forecast fact | not provided in source reports |
| Section 2 | COPPER_CONTEXT | copper | latest broad copper price, inventory, demand, supply, or forecast fact | not provided in source reports |
| Section 2 | AGRICULTURE_CONTEXT | agriculture | latest broad agriculture price, crop, WASDE, or supply fact | not provided in source reports |
| Section 2 | BROAD_COMMODITIES_CONTEXT | broad commodities | latest broad commodity index, World Bank, or commodity-market fact | not provided in source reports |
| Section 2 | EURO_CONTEXT | euro | latest ECB, EUR/USD, euro-area rate, or currency fact | not provided in source reports |
| Section 2 | YEN_CONTEXT | yen | latest BOJ, USD/JPY, Japan rate, or currency fact | not provided in source reports |
| Section 2 | SOFTWARE_CONTEXT | software | latest broad software price, spending, revenue, or sector fact | not provided in source reports |
| Section 2 | BROAD_AI_TECH_CONTEXT | broad AI technology | latest broad AI spending, investment, infrastructure, or policy fact | not provided in source reports |
| Section 2 | AUTONOMOUS_ROBOTICS_CONTEXT | autonomous technology / robotics | latest robotics order, automation, industrial robot, or policy fact | not provided in source reports |
| Section 2 | CYBERSECURITY_CONTEXT | cybersecurity | latest broad cybersecurity spending, incident count, policy, or sector fact | not provided in source reports |
| Section 2 | SOLAR_CONTEXT | solar | latest solar generation, installation, capacity, policy, or forecast fact | not provided in source reports |
| Section 3 | NEXT_MAJOR_COUNTRY_INFLATION_RELEASES | broad US equities; bonds and rates; TIPS; consumer sectors | not scheduled inside scoring window | not_scheduled_inside_window |
| Section 3 | NEXT_MAJOR_COUNTRY_GDP_RELEASES | broad US equities | not scheduled inside scoring window | not_scheduled_inside_window |
| Section 3 | NEXT_MAJOR_COUNTRY_PMI_RELEASES | broad US equities; industrials | not scheduled inside scoring window | not_scheduled_inside_window |
| Section 3 | NEXT_MAJOR_BROAD_INDEX_EARNINGS_MILESTONE | broad US equities | not scheduled inside scoring window | not_scheduled_inside_window |
| Section 3 | NEXT_MAJOR_SECTOR_POLICY_EVENTS | healthcare; sector policy | not scheduled inside scoring window | not_scheduled_inside_window |
| Section 3 | NEXT_MAJOR_CRYPTO_REGULATORY_OR_ETF_EVENTS | bitcoin proxy; ethereum proxy | not scheduled inside scoring window | not_scheduled_inside_window |
