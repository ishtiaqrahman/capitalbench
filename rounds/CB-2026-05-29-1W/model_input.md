# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make one-shot market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-week outcome window resolves.

The scoring timeline is central to the task. This is a one-week, Friday-to-Friday round:
- Research cutoff: 2026-05-29T22:45:00Z.
- Decision deadline: 2026-05-30T00:00:00Z.
- Entry price: adjusted close on Friday, May 29, 2026.
- Exit price: adjusted close on Friday, June 5, 2026.
- Results are calculated only after regular U.S. trading ends on June 5, 2026.

The portfolio is measured from the May 29, 2026 adjusted close to the June 5, 2026 adjusted close. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before the June 5, 2026 exit close.

Optimize only for the portfolio you expect to perform best over this close-to-close one-week scoring window. Use longer-horizon facts only when they are likely to affect prices before the June 5, 2026 exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical return table. Treat inclusion, section order, grouping, row count, and trailing-return table order as context, not recommendation signals.

Your objective is to allocate 100% across the allowed options to maximize expected one-week realized portfolio return, measured from the May 29, 2026 adjusted close to the June 5, 2026 adjusted close, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official one-shot leaderboard.

Your portfolio is scored by the weighted realized percentage return over the one-week round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

You may use your internal learned knowledge and general market priors. Do not browse, use tools, request updated market data, use external retrieval, or intentionally rely on facts, market prices, news, or events dated after the research cutoff. If your internal knowledge conflicts with the briefing, prioritize the briefing.

You must allocate exactly 100% across allowed options. Use only the holding count, allocation increment, minimum allocation, and cash or benchmark constraints stated in the round metadata. Do not short, use leverage, or choose an option outside the allowed option list.

Return only valid JSON. Do not include markdown, prose, citations, or commentary outside the JSON.

Required JSON format:

{
  "round_id": "<round_id>",
  "model_id": "<model_id>",
  "provider": "<provider>",
  "mode": "closed_capability",
  "portfolio": [
    {
      "option_id": "<one allowed option ID>",
      "allocation_pct": <integer percentage>,
      "rationale": "<brief holding-level rationale>"
    }
  ],
  "confidence": <number from 0 to 1>,
  "portfolio_rationale": "<1-3 sentence allocation rationale>",
  "rationale_summary": "<1-3 sentence rationale>",
  "key_risks": [
    "<risk 1>",
    "<risk 2>"
  ]
}

Rules:
- portfolio must contain only IDs from the allowed option list.
- allocation_pct values must be integers in the stated allocation increment.
- allocation_pct values must sum to exactly 100.
- confidence must be between 0 and 1.
- confidence should reflect your confidence that this is the best portfolio decision under the round constraints.
- portfolio_rationale and rationale_summary are required and should be concise.
- key_risks must be a list of 2-5 concrete risks that could cause the portfolio to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup portfolio, second-best portfolio, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.

## Round Metadata

- Round ID: CB-2026-05-29-1W
- Decision date: 2026-05-29
- Research cutoff UTC: 2026-05-29T22:45:00Z
- Decision deadline UTC: 2026-05-30T00:00:00Z
- Horizon: one week
- Entry date: 2026-05-29
- Exit date: 2026-06-05
- Scoring window: 2026-05-29 to 2026-06-05; optimize for this one week window only.
- Close-to-close scoring: the entry price is the adjusted close on the entry date, and the exit price is the adjusted close on the exit date after regular trading ends.
- Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.
- Input-bias control: treat fact inclusion, section order, grouping, and trailing-return table order as context, not recommendations; do not infer expected return from mention count or placement.
- Entry rule: Use adjusted close on Friday, May 29, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Friday, June 5, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Submission format: portfolio
- Scoring benchmark: S&P 500 / SPY
- Return calculation: adjusted close prices are used when available.
- Portfolio holdings allowed: 1-5
- Portfolio allocation increment: 5%
- Portfolio minimum allocation: 5%
- Portfolio total allocation: 100%

## Briefing

# CapitalBench Briefing

## 1. Neutrality And Bias-Control Statement

This briefing provides factual market context only. It does not rank or recommend any CapitalBench option. Some facts are grouped by broad asset area for readability; inclusion, order, and grouping are not evidence of expected return.

## 2. Research And Evaluation Setup

| field | value |
| --- | --- |
| research cutoff | 2026-05-29T22:45:00Z |
| decision deadline | 2026-05-30T00:00:00Z |
| evaluation horizon | one week |
| model access rule | no tool use and no web access |
| shared-input rule | competing models receive the same frozen factual briefing, fixed ETF option universe, and mechanical return table |

## 3. Macro, Rates, Credit, Liquidity, And Volatility

### Core Macro Table

| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inflation | CPI-U, all items | 0.6% | 0.9% in March 2026 | prior value | April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | CPI-U, all items | 3.8% | 3.3% for the 12 months ending March 2026 | prior value | 12 months ending April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | CPI-U, all items less food and energy | 0.4% | 0.2% in March 2026 | prior value | April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | CPI-U, all items less food and energy | 2.8% | 2.6% for the 12 months ending March 2026 | prior value | 12 months ending April 2026 | May 12, 2026 | BLS CPI News Release |
| inflation | PCE price index | 0.4% | 0.7% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays |
| inflation | PCE price index | 3.8% | not source-reported | not source-reported | April 2026 from same month one year ago | May 28, 2026 | BEA Personal Income and Outlays |
| inflation | PCE price index excluding food and energy | 0.2% | 0.3% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays |
| inflation | PCE price index excluding food and energy | 3.3% | not source-reported | not source-reported | April 2026 from same month one year ago | May 28, 2026 | BEA Personal Income and Outlays |
| inflation | Producer Price Index for final demand | 1.4% | 0.7% in March 2026 and 0.6% in February 2026 | prior value | April 2026 | May 13, 2026 | BLS Producer Price Index |
| inflation | Producer Price Index for final demand | 6.0% | 4.3% in March 2026 | prior value | 12 months ending April 2026 | May 13, 2026 | BLS Producer Price Index |
| labor | unemployment rate | 4.3% | unchanged at 4.3% | prior value | April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | nonfarm payroll employment | +115,000 jobs | March 2026 revised to +185,000 jobs | prior value | April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | average hourly earnings for all employees on private nonfarm payrolls | $37.41 | +0.2% over the month and +3.6% over the year | month-over-month and year-over-year change | April 2026 | May 8, 2026 | BLS Employment Situation |
| labor | seasonally adjusted initial unemployment insurance claims | 215,000 | increase of 5,000 from the previous week's revised level | week-over-week change | week ending May 23, 2026 | May 28, 2026 | U.S. Department of Labor UI Claims |
| growth | real GDP | +1.6% annual rate | revised down 0.4 percentage point from the advance estimate; Q4 2025 was +0.5% | revision and prior value | Q1 2026 second estimate | May 28, 2026 | BEA GDP Second Estimate |
| growth | retail and food services sales | $757.1 billion | up 0.5% from previous month and up 4.9% from April 2025 | month-over-month and year-over-year change | April 2026 | May 14, 2026 | U.S. Census Monthly Retail Trade |
| growth | current-dollar personal consumption expenditures | +$111.1 billion; +0.5% | 1.0% in March 2026 | prior value | April 2026 | May 28, 2026 | BEA Personal Income and Outlays |
| growth | industrial production | 102.5 index; +0.7% | -0.3% in March 2026; 1.4% above April 2025 | prior value and year-over-year change | April 2026 | May 15, 2026 | Federal Reserve G.17 |
| business surveys | ISM Manufacturing PMI | 52.7 | same reading as March 2026 | prior value | April 2026 | May 1, 2026 | ISM Manufacturing PMI |
| business surveys | ISM Services PMI | 53.6 | 54.0 in March 2026 | prior value | April 2026 | May 5, 2026 | ISM Services PMI |
| consumer | University of Michigan Index of Consumer Sentiment | 44.8 | 49.8 in April 2026 and 52.2 in May 2025 | prior value and year-over-year change | May 2026 final | May 22, 2026 | University of Michigan Surveys of Consumers |
| consumer | Conference Board Consumer Confidence Index | 93.1 | down 0.7 points from upwardly revised 93.8 in April 2026 | prior value | May 2026 | May 26, 2026 | The Conference Board Consumer Confidence |
| housing | housing starts | 1,465,000 SAAR | down 2.8% from revised March 2026 and up 4.6% from April 2025 | month-over-month and year-over-year change | April 2026 | May 21, 2026 | Census/HUD New Residential Construction |
| housing | building permits | 1,442,000 SAAR | up 5.8% from revised March 2026 and down 0.2% from April 2025 | month-over-month and year-over-year change | April 2026 | May 21, 2026 | Census/HUD New Residential Construction |
| housing | existing-home sales | 4.02 million sales | increased by 0.2% in April 2026 | month-over-month change | April 2026 | May 2026 | National Association of Realtors Existing-Home Sales |

### Rates, Fed, Credit, Liquidity, And Volatility

| data_area | measure | latest_value | source_reported_comparison | comparison_type | period_covered | release_or_observation_date | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Federal Reserve policy | federal funds target range | 3.50% to 3.75% | not source-reported | not source-reported | current target range | April 29, 2026 | Federal Reserve FOMC Statement |
| Federal Reserve policy | latest FOMC decision | maintain target range at 3.50% to 3.75% | not source-reported | not source-reported | April 2026 FOMC meeting | April 29, 2026 | Federal Reserve FOMC Statement |
| Federal Reserve policy | effective federal funds rate | 3.62% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED DFF |
| Treasury yields | 3-month Treasury constant maturity rate | 3.69% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED DGS3MO |
| Treasury yields | 2-year Treasury constant maturity rate | 3.99% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED DGS2 |
| Treasury yields | 10-year Treasury constant maturity rate | 4.45% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED DGS10 |
| Treasury yields | 30-year Treasury constant maturity rate | 4.98% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED DGS30 |
| real rates | 10-year Treasury inflation-indexed security constant maturity rate | 2.06% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED DFII10 |
| inflation expectations | 10-year breakeven inflation rate | 2.39% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED T10YIE |
| Treasury spreads | 10-year Treasury minus 2-year Treasury constant maturity spread | 0.46 percentage point | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED T10Y2Y |
| currency | U.S. Dollar Index futures | 98.890 | not source-reported | not source-reported | May 29, 2026 | May 29, 2026 22:58:59 source time | Stooq DX.F Quote |
| volatility | CBOE Volatility Index | 15.74 | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED VIXCLS |
| credit spreads | ICE BofA US Corporate Index option-adjusted spread | 0.73% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED BAMLC0A0CM |
| credit spreads | ICE BofA US High Yield Index option-adjusted spread | 2.72% | not source-reported | not source-reported | May 28, 2026 | May 28, 2026 | FRED BAMLH0A0HYM2 |
| financial conditions | Chicago Fed National Financial Conditions Index | -0.510 | not source-reported | not source-reported | week ending May 22, 2026 | May 22, 2026 | FRED NFCI |
| liquidity | total money market fund assets | $7.77 trillion | increased by $16.88 billion | week-over-week change | week ending May 20, 2026 | May 21, 2026 | Investment Company Institute Money Market Fund Assets |
| liquidity | Federal Reserve total assets | $6.704383 trillion | not source-reported | not source-reported | week ending May 27, 2026 | May 27, 2026 | FRED WALCL |
| liquidity | Treasury General Account balance | $830.296 billion | not source-reported | not source-reported | week ending May 27, 2026 | May 27, 2026 | FRED WTREGEN |
| housing rates | 30-year fixed-rate mortgage average | 6.53% | 6.51% previous week | prior value | week ending May 28, 2026 | May 28, 2026 | FRED MORTGAGE30US |

### Commodity And Currency State

| measure | latest_value | source_reported_comparison | comparison_type | observation_date | source |
| --- | --- | --- | --- | --- | --- |
| WTI crude futures | $87.76 per barrel | not source-reported | not source-reported | May 29, 2026 22:59:57 source time | Stooq CL.F Quote |
| Brent crude spot | $102.75 per barrel | not source-reported | not source-reported | May 26, 2026 | FRED DCOILBRENTEU |
| natural gas futures | $3.290 per MMBtu | not source-reported | not source-reported | May 29, 2026 23:38:24 source time | Stooq NG.F Quote |
| gold futures | $4,569.90 per t oz | not source-reported | not source-reported | May 29, 2026 22:59:58 source time | Stooq GC.F Quote |
| silver futures | 7,556.7 USd per t oz | not source-reported | not source-reported | May 29, 2026 22:58:59 source time | Stooq SI.F Quote |
| high grade copper futures | 639.63 USd per lb | not source-reported | not source-reported | May 29, 2026 22:58:59 source time | Stooq HG.F Quote |
| U.S. Dollar Index futures | 98.890 | not source-reported | not source-reported | May 29, 2026 22:58:59 source time | Stooq DX.F Quote |
| euro / U.S. dollar | 1.16646 | not source-reported | not source-reported | May 29, 2026 22:00:20 source time | Stooq EURUSD Quote |
| U.S. dollar / Japanese yen | 159.2635 | not source-reported | not source-reported | May 29, 2026 22:00:28 source time | Stooq USDJPY Quote |

## 4. Scheduled Calendar Inside The Scoring Window

| date | event | publisher_or_entity | release_type_or_asset_area | consensus_or_forecast_if_source_reported | source |
| --- | --- | --- | --- | --- | --- |
| June 1, 2026 10:00 AM ET | ISM Manufacturing PMI, May 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar |
| June 3, 2026 10:00 AM ET | ISM Services PMI, May 2026 | Institute for Supply Management | business survey release | not source-reported | ISM Report Calendar |
| June 5, 2026 8:30 AM ET | Employment Situation, May 2026 | U.S. Bureau of Labor Statistics | labor market release | not source-reported | BLS Employment Situation |

## 5. Balanced Asset-Area Context

| asset_area | covered_area | fact_type | balance_role | factual_statement | source_reported_comparison | comparison_type | date_or_period | source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cash and short-duration Treasuries | federal funds and short bills | policy_or_regulatory_fact | current_condition | The FOMC maintained the federal funds target range at 3.50% to 3.75%. | not source-reported | not source-reported | April 29, 2026 | Federal Reserve FOMC Statement |
| bonds and rates | Treasury curve | observed_value | current_condition | The 3-month, 2-year, 10-year, and 30-year Treasury constant maturity rates were 3.69%, 3.99%, 4.45%, and 4.98%, respectively. | not source-reported | not source-reported | May 28, 2026 | FRED Treasury Rates |
| credit | corporate credit | observed_value | current_condition | The ICE BofA US Corporate Index option-adjusted spread was 0.73%, and the ICE BofA US High Yield Index option-adjusted spread was 2.72%. | not source-reported | not source-reported | May 28, 2026 | FRED BAMLC0A0CM and BAMLH0A0HYM2 |
| broad US equities | corporate profits | observed_value | current_condition | Profits from current production increased $40.4 billion in Q1 2026. | $246.9 billion increase in Q4 2025 | prior value | Q1 2026 second estimate | BEA GDP Second Estimate |
| broad US equities | real GDP | observed_value | counterbalancing_fact | Real GDP increased at a 1.6% annual rate in Q1 2026. | revised down 0.4 percentage point from the advance estimate; Q4 2025 was +0.5% | revision and prior value | Q1 2026 second estimate | BEA GDP Second Estimate |
| financials and regional banks | banking industry | observed_value | current_condition | FDIC-insured institutions reported a 1.26% return on assets ratio and $80.5 billion of aggregate net income. | net income increased $2.8 billion, or 3.6%, from the prior quarter | prior value | Q1 2026 | FDIC Quarterly Banking Profile |
| consumer sectors | consumer spending | observed_value | current_condition | Current-dollar personal consumption expenditures increased $111.1 billion, or 0.5%. | 1.0% in March 2026 | prior value | April 2026 | BEA Personal Income and Outlays |
| consumer sectors | consumer sentiment | observed_value | counterbalancing_fact | The University of Michigan Index of Consumer Sentiment was 44.8. | 49.8 in April 2026 and 52.2 in May 2025 | prior value and year-over-year change | May 2026 final | University of Michigan Surveys of Consumers |
| real estate | housing construction | observed_value | current_condition | Housing starts were 1,465,000 SAAR, and building permits were 1,442,000 SAAR. | starts down 2.8%; permits up 5.8% from March 2026 | month-over-month change | April 2026 | Census/HUD New Residential Construction |
| real estate | mortgage reference rates | observed_value | counterbalancing_fact | The 30-year fixed-rate mortgage average was 6.53%. | 6.51% previous week | prior value | week ending May 28, 2026 | FRED MORTGAGE30US |
| software | software prices | observed_value | current_condition | The PCE Computer Software and Accessories category increased 13.9% year over year and roughly 73.1% annualized from November 2025 through March 2026. | average annualized rate of -5.3% over the prior 25 years | prior value | November 2025 through March 2026 | Federal Reserve FEDS Notes |
| semiconductors | global chip sales | observed_value | current_condition | Global semiconductor sales were $298.5 billion during Q1 2026. | up 25% compared to Q4 2025 | prior value | Q1 2026 | Semiconductor Industry Association |
| energy and oil | crude oil outlook | labeled_forecast_or_estimate | current_condition | EIA forecast global oil inventories would decrease by 2.6 million barrels per day in 2026. | last month's STEO forecast a 0.3 million barrel per day decrease | prior value | May 2026 Short-Term Energy Outlook | EIA STEO |
| energy and oil | OPEC supply policy | policy_or_regulatory_fact | counterbalancing_fact | Seven OPEC+ countries decided to implement a production adjustment of 188 thousand barrels per day from previous voluntary adjustments. | not source-reported | not source-reported | decision on May 3, 2026; adjustment for June 2026 | OPEC |
| currencies | U.S. dollar, euro, and yen | observed_value | current_condition | U.S. Dollar Index futures, EUR/USD, and USD/JPY were quoted at 98.890, 1.16646, and 159.2635, respectively. | not source-reported | not source-reported | May 29, 2026 | Stooq Currency Quotes |
| crypto proxies | bitcoin and ethereum | observed_value | current_condition | Bitcoin and ethereum were quoted at 73,346.17 and 2,008.484, respectively. | not source-reported | not source-reported | May 30, 2026 source time | Stooq Crypto Quotes |
| Europe equities | euro area policy | policy_or_regulatory_fact | current_condition | The ECB held the deposit facility, main refinancing operations, and marginal lending facility rates at 2.00%, 2.15%, and 2.40%, respectively. | not source-reported | not source-reported | April 30, 2026 | European Central Bank |
| Japan equities | Japan policy rate | policy_or_regulatory_fact | current_condition | The Bank of Japan encouraged the uncollateralized overnight call rate to remain at around 0.75%. | not source-reported | not source-reported | April 28, 2026 | Bank of Japan Monetary Policy Statement |
| China equities | credit policy and manufacturing survey | policy_or_regulatory_fact | current_condition | China's one-year Loan Prime Rate was 3.0%, and its five-year Loan Prime Rate was 3.5%; China's official manufacturing PMI was 50.3 in April 2026. | manufacturing PMI down 0.1 percentage point from the previous month | month-over-month change | May 2026 LPR; April 2026 PMI | Trading Economics China Interest Rate; National Bureau of Statistics of China PMI |
| India equities | inflation and monetary policy | observed_value | current_condition | India's April 2026 CPI inflation was 3.48%, and the Reserve Bank of India policy repo rate was 5.25%. | CPI was 3.40% in March 2026 | prior value | April 2026 CPI; April 2026 monetary policy | Press Information Bureau India CPI; Reserve Bank of India Current Rates |

## 6. Factual Tension Ledger

| area_or_asset_area | source_reported_fact_1 | source_reported_fact_2 | unresolved_question | source_or_sources |
| --- | --- | --- | --- | --- |
| labor and inflation | unemployment rate was unchanged at 4.3% in April 2026 | CPI-U all items rose 3.8% over the 12 months ending April 2026 | May 2026 Employment Situation release on June 5, 2026 | BLS Employment Situation; BLS CPI News Release |

## 7. Source-Reported Uncertainties And Missing Major Data

### Source-Reported Uncertainties

| uncertainty | source-reported wording or concise factual paraphrase | source date if provided | status |
| --- | --- | --- | --- |
| labor release outcome | The May 2026 Employment Situation was scheduled but not included as released data in the input reports. | May 2026 source reports | source_reported_uncertainty |
| business survey outcomes | May 2026 ISM Manufacturing PMI and ISM Services PMI releases were scheduled but not included as released data in the input reports. | May 2026 source reports | source_reported_uncertainty |

### Missing Major Data

| data_area | missing_item | note |
| --- | --- | --- |
| labor | May 2026 Employment Situation | not provided in source reports |
| business surveys | May 2026 ISM Manufacturing PMI and ISM Services PMI | not provided in source reports |

## 8. Full-Universe Trailing Returns

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-05-29 | 0.00% | 0.00% | 0.00% | 0.00% | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-05-29 | 0.08% | 0.33% | 1.81% | 3.92% | pass |
| SP500 | SPY | us_broad_market | 2026-05-29 | 1.45% | 6.31% | 11.33% | 29.68% | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-05-29 | 1.57% | 6.38% | 11.44% | 29.93% | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-05-29 | 2.89% | 11.60% | 19.53% | 42.68% | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-05-29 | 2.28% | 7.62% | 7.54% | 28.41% | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-05-29 | 0.69% | 4.80% | 14.31% | 28.47% | pass |
| MID_CAP | IJH | us_size_factor | 2026-05-29 | 1.50% | 4.23% | 13.27% | 25.43% | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-05-29 | 1.86% | 6.74% | 17.36% | 42.42% | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-05-29 | 1.21% | 4.77% | 18.37% | 43.44% | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-05-29 | -1.01% | 3.34% | 19.99% | 28.88% | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-05-29 | -2.54% | -2.07% | -0.22% | 0.95% | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-05-29 | 4.02% | 13.72% | 26.65% | 38.22% | pass |
| TECHNOLOGY | XLK | us_sector | 2026-05-29 | 5.89% | 20.06% | 33.84% | 65.87% | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-05-29 | 0.20% | 0.35% | 0.90% | 15.98% | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-05-29 | 1.42% | 3.45% | 2.63% | 13.33% | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-05-29 | -2.23% | -0.01% | 5.89% | 3.77% | pass |
| HEALTHCARE | XLV | us_sector | 2026-05-29 | -0.28% | 4.64% | -4.40% | 14.94% | pass |
| FINANCIALS | XLF | us_sector | 2026-05-29 | -0.69% | -0.65% | -2.45% | 2.99% | pass |
| INDUSTRIALS | XLI | us_sector | 2026-05-29 | 0.79% | 1.88% | 13.34% | 22.92% | pass |
| ENERGY | XLE | us_sector | 2026-05-29 | -5.38% | -4.64% | 26.33% | 41.26% | pass |
| MATERIALS | XLB | us_sector | 2026-05-29 | 1.71% | 0.37% | 15.52% | 20.80% | pass |
| UTILITIES | XLU | us_sector | 2026-05-29 | -2.05% | -2.76% | -0.56% | 12.65% | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-05-29 | -1.28% | 0.80% | 7.43% | 9.16% | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-05-29 | 0.82% | 0.17% | -1.06% | 4.29% | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-05-29 | 1.28% | 0.44% | -2.78% | 4.08% | pass |
| TIPS | TIP | bonds_and_rates | 2026-05-29 | 0.75% | 0.34% | 1.07% | 5.01% | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-05-29 | 0.91% | 0.97% | 0.02% | 6.45% | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-05-29 | 0.50% | 0.75% | 2.10% | 7.08% | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-05-29 | 0.63% | 0.43% | 0.21% | 5.29% | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-05-29 | 1.86% | 6.99% | 18.74% | 33.39% | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-05-29 | 1.53% | 3.10% | 12.42% | 29.42% | pass |
| EUROPE | VGK | international_equity | 2026-05-29 | 0.62% | 4.55% | 10.73% | 19.76% | pass |
| JAPAN | EWJ | international_equity | 2026-05-29 | 1.47% | 7.08% | 16.23% | 31.38% | pass |
| CHINA | MCHI | international_equity | 2026-05-29 | -0.79% | -3.04% | -10.32% | 4.57% | pass |
| INDIA | INDA | international_equity | 2026-05-29 | 0.35% | -0.96% | -11.24% | -11.05% | pass |
| GOLD | IAU | commodities | 2026-05-29 | 0.80% | -0.07% | 7.66% | 36.70% | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-05-29 | -3.19% | -4.76% | 33.06% | 44.74% | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-05-29 | 3.92% | 19.89% | 70.54% | 146.14% | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-05-29 | 8.14% | 20.31% | -2.33% | -0.67% | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-05-29 | 7.18% | 22.31% | 34.38% | 66.76% | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-05-29 | 4.86% | 15.91% | 30.27% | 78.45% | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-05-29 | 5.65% | 31.19% | 21.45% | 26.08% | pass |
| SOLAR | TAN | clean_energy | 2026-05-29 | 12.10% | 31.74% | 51.16% | 131.54% | pass |
| METALS_MINING | XME | commodities | 2026-05-29 | 6.95% | 9.25% | 29.20% | 108.43% | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-05-29 | 1.09% | 4.20% | 9.93% | 20.29% | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-05-29 | 3.82% | 6.04% | 11.34% | 70.50% | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-05-29 | 0.35% | 0.84% | 11.83% | 24.56% | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-05-29 | 4.47% | 10.46% | 14.87% | 34.25% | pass |
| CANADA | EWC | country_equity | 2026-05-29 | 0.51% | 3.21% | 12.59% | 33.39% | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-05-29 | -0.34% | 2.04% | 10.87% | 22.69% | pass |
| AUSTRALIA | EWA | country_equity | 2026-05-29 | 1.63% | 2.20% | 15.10% | 17.81% | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-05-29 | 13.07% | 33.69% | 131.66% | 240.64% | pass |
| TAIWAN | EWT | country_equity | 2026-05-29 | 6.13% | 17.88% | 66.67% | 103.36% | pass |
| BRAZIL | EWZ | country_equity | 2026-05-29 | -1.26% | -7.09% | 10.68% | 36.74% | pass |
| MEXICO | EWW | country_equity | 2026-05-29 | 0.86% | 4.02% | 16.86% | 32.95% | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-05-29 | 3.12% | 4.41% | 9.72% | 39.66% | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-05-29 | 0.75% | 0.55% | 1.09% | 7.00% | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-05-29 | 0.94% | 0.39% | 1.37% | 6.41% | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-05-29 | 1.32% | 1.41% | 2.26% | 12.02% | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-05-29 | 0.56% | 1.22% | 0.40% | 2.27% | pass |
| SILVER | SLV | commodities | 2026-05-29 | -0.04% | 5.38% | 33.43% | 125.51% | pass |
| COPPER | CPER | commodities | 2026-05-29 | -0.15% | 8.03% | 20.38% | 33.26% | pass |
| AGRICULTURE | DBA | commodities | 2026-05-29 | -1.12% | -3.06% | 6.84% | 6.24% | pass |
| OIL | USO | commodities | 2026-05-29 | -8.39% | -14.30% | 81.64% | 92.13% | pass |
| US_DOLLAR | UUP | currencies | 2026-05-29 | -0.40% | 0.18% | 1.41% | 4.18% | pass |
| EURO | FXE | currencies | 2026-05-29 | 0.56% | 0.02% | 0.93% | 3.39% | pass |
| YEN | FXY | currencies | 2026-05-29 | -0.14% | 0.63% | -2.21% | -9.83% | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-05-29 | -3.10% | -2.62% | -19.24% | -30.61% | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-05-29 | -2.38% | -9.79% | -33.77% | -24.34% | pass |

## 9. Coverage And Bias Audit

| asset_area | final_rows_in_briefing | current_condition_rows | counterbalancing_or_uncertainty_rows | scheduled_event_rows | note |
| --- | --- | --- | --- | --- | --- |
| cash and short-duration Treasuries | 1 | 1 | 0 | 0 | one final row retained |
| bonds and rates | 2 | 1 | 0 | 1 | final rows preserved from asset-area context |
| credit | 1 | 1 | 0 | 0 | one final row retained |
| broad US equities | 2 | 1 | 1 | 0 | final rows preserved from asset-area context |
| financials and regional banks | 1 | 1 | 0 | 0 | one final row retained |
| consumer sectors | 2 | 1 | 1 | 0 | rows trimmed to maintain balance or fit horizon |
| real estate | 2 | 1 | 1 | 0 | final rows preserved from asset-area context |
| software | 1 | 1 | 0 | 0 | one final row retained |
| semiconductors | 1 | 1 | 0 | 0 | one final row retained |
| energy and oil | 2 | 1 | 1 | 0 | final rows preserved from asset-area context |
| currencies | 1 | 1 | 0 | 0 | one final row retained |
| crypto proxies | 1 | 1 | 0 | 0 | one final row retained |
| Europe equities | 1 | 1 | 0 | 0 | one final row retained |
| Japan equities | 1 | 1 | 0 | 0 | one final row retained |
| China equities | 1 | 1 | 0 | 0 | one final row retained |
| India equities | 1 | 1 | 0 | 0 | one final row retained |

## 10. Final Neutrality Statement

This briefing provides factual market context only. It does not rank or recommend any CapitalBench option. Some facts are grouped by broad asset area for readability; inclusion, order, and grouping are not evidence of expected return.

## Options

Allowed option:
ID: CASH
Name: Cash / Do Not Invest
Symbol: N/A
Asset class: cash
Category: cash
Group: cash
Risk bucket: cash
Description: Cash position with no market exposure. Return is treated as 0 unless a round explicitly defines a cash yield proxy.

Allowed option:
ID: SHORT_TREASURY
Name: Short-Term Treasury Bills
Symbol: BIL
Asset class: cash_like
Category: treasury_bills
Group: cash_and_short_duration
Risk bucket: low
Description: Short-term US Treasury bill exposure. Typically used as a cash-like proxy with low duration risk.

Allowed option:
ID: SP500
Name: S&P 500
Symbol: SPY
Asset class: equity
Category: broad_us_equity
Group: us_broad_market
Risk bucket: medium
Description: Broad US large-cap equity exposure. Represents large publicly traded US companies across multiple sectors.

Allowed option:
ID: TOTAL_US_MARKET
Name: Total US Stock Market
Symbol: VTI
Asset class: equity
Category: broad_us_equity
Group: us_broad_market
Risk bucket: medium
Description: Broad exposure to the total US equity market, including large-, mid-, and small-cap companies. Useful as a diversified US equity proxy.

Allowed option:
ID: NASDAQ100
Name: Nasdaq 100
Symbol: QQQ
Asset class: equity
Category: growth_equity
Group: us_growth_and_technology
Risk bucket: high
Description: Large-cap, growth-oriented US equity exposure with heavy weights in technology and communication services. Sensitive to mega-cap earnings, rates, and growth-stock sentiment.

Allowed option:
ID: LARGE_GROWTH
Name: US Large-Cap Growth
Symbol: IWF
Asset class: equity
Category: style_factor
Group: us_style_factor
Risk bucket: high
Description: US large-cap growth stock exposure. Often tilted toward companies with higher expected growth, higher valuations, and greater sensitivity to interest rates.

Allowed option:
ID: LARGE_VALUE
Name: US Large-Cap Value
Symbol: IWD
Asset class: equity
Category: style_factor
Group: us_style_factor
Risk bucket: medium
Description: US large-cap value stock exposure. Often tilted toward companies with lower valuation multiples, dividends, financials, energy, and cyclical sectors.

Allowed option:
ID: MID_CAP
Name: US Mid-Cap Stocks
Symbol: IJH
Asset class: equity
Category: size_factor
Group: us_size_factor
Risk bucket: high
Description: US mid-cap equity exposure. Represents companies between large caps and small caps, with sensitivity to domestic growth, financing conditions, and risk appetite.

Allowed option:
ID: SMALL_CAP
Name: US Small-Cap Stocks
Symbol: IWM
Asset class: equity
Category: size_factor
Group: us_size_factor
Risk bucket: high
Description: US small-cap equity exposure. Often more sensitive to domestic economic growth, credit conditions, rates, and market risk appetite.

Allowed option:
ID: SMALL_VALUE
Name: US Small-Cap Value
Symbol: IWN
Asset class: equity
Category: style_and_size_factor
Group: us_style_factor
Risk bucket: high
Description: US small-cap value equity exposure. Combines smaller company exposure with value-oriented characteristics.

Allowed option:
ID: DIVIDEND
Name: US Dividend Equities
Symbol: SCHD
Asset class: equity
Category: dividend_equity
Group: us_factor_equity
Risk bucket: medium
Description: US dividend-oriented equity exposure. Often tilted toward profitable, mature companies with dividend histories.

Allowed option:
ID: LOW_VOL
Name: US Low Volatility Equities
Symbol: SPLV
Asset class: equity
Category: low_volatility_factor
Group: us_factor_equity
Risk bucket: medium
Description: US equity exposure focused on historically lower-volatility stocks. Often used as a defensive equity factor proxy.

Allowed option:
ID: MOMENTUM
Name: US Momentum Equities
Symbol: MTUM
Asset class: equity
Category: momentum_factor
Group: us_factor_equity
Risk bucket: high
Description: US equity exposure tilted toward stocks with stronger recent price momentum. Sensitive to trend persistence and factor rotations.

Allowed option:
ID: TECHNOLOGY
Name: Technology Sector
Symbol: XLK
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US technology sector exposure within large-cap equities. Includes software, hardware, semiconductors, and technology services companies.

Allowed option:
ID: COMMUNICATIONS
Name: Communication Services Sector
Symbol: XLC
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US communication services sector exposure. Includes large internet platforms, media, telecom, and entertainment companies.

Allowed option:
ID: CONSUMER_DISCRETIONARY
Name: Consumer Discretionary Sector
Symbol: XLY
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US consumer discretionary sector exposure. Sensitive to consumer spending, employment, credit conditions, and household confidence.

Allowed option:
ID: CONSUMER_STAPLES
Name: Consumer Staples Sector
Symbol: XLP
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US consumer staples sector exposure. Includes companies selling essential consumer products and is often considered a defensive equity sector.

Allowed option:
ID: HEALTHCARE
Name: Healthcare Sector
Symbol: XLV
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US healthcare sector exposure. Includes pharmaceuticals, biotechnology, medical devices, healthcare services, and insurers.

Allowed option:
ID: FINANCIALS
Name: Financials Sector
Symbol: XLF
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US financial sector exposure. Includes banks, insurers, capital markets firms, and financial services companies.

Allowed option:
ID: INDUSTRIALS
Name: Industrials Sector
Symbol: XLI
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US industrial sector exposure. Includes aerospace, machinery, transportation, logistics, and industrial services companies.

Allowed option:
ID: ENERGY
Name: Energy Sector
Symbol: XLE
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US energy sector exposure. Sensitive to oil and gas prices, production trends, geopolitics, and capital discipline.

Allowed option:
ID: MATERIALS
Name: Materials Sector
Symbol: XLB
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US materials sector exposure. Includes chemicals, metals, mining, packaging, and construction materials companies.

Allowed option:
ID: UTILITIES
Name: Utilities Sector
Symbol: XLU
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: medium
Description: US utilities sector exposure. Often sensitive to interest rates, electricity demand, regulation, and defensive equity flows.

Allowed option:
ID: REAL_ESTATE
Name: Real Estate Sector
Symbol: XLRE
Asset class: equity
Category: us_sector
Group: us_sector
Risk bucket: high
Description: US listed real estate equity exposure. Sensitive to interest rates, property fundamentals, credit conditions, and real estate valuations.

Allowed option:
ID: INTERMEDIATE_TREASURY
Name: Intermediate-Term US Treasury Bonds
Symbol: IEF
Asset class: bond
Category: treasury_duration
Group: bonds_and_rates
Risk bucket: medium
Description: Intermediate-duration US Treasury bond exposure. Sensitive to changes in interest rates, inflation expectations, and growth expectations.

Allowed option:
ID: LONG_TREASURY
Name: Long-Term US Treasury Bonds
Symbol: TLT
Asset class: bond
Category: treasury_duration
Group: bonds_and_rates
Risk bucket: high
Description: Long-duration US Treasury bond exposure. More sensitive to interest-rate changes than shorter-duration bond funds.

Allowed option:
ID: TIPS
Name: Treasury Inflation-Protected Securities
Symbol: TIP
Asset class: bond
Category: inflation_linked_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: US Treasury inflation-protected bond exposure. Sensitive to real interest rates and inflation expectations.

Allowed option:
ID: INVESTMENT_GRADE_CREDIT
Name: Investment Grade Corporate Bonds
Symbol: LQD
Asset class: bond
Category: corporate_credit
Group: credit
Risk bucket: medium
Description: US investment-grade corporate bond exposure. Sensitive to interest rates, credit spreads, and corporate balance-sheet conditions.

Allowed option:
ID: HIGH_YIELD_CREDIT
Name: High Yield Corporate Bonds
Symbol: HYG
Asset class: bond
Category: corporate_credit
Group: credit
Risk bucket: high
Description: US high-yield corporate bond exposure. Sensitive to credit spreads, default expectations, liquidity, and risk appetite.

Allowed option:
ID: AGGREGATE_BONDS
Name: US Aggregate Bond Market
Symbol: AGG
Asset class: bond
Category: aggregate_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: Broad US investment-grade bond market exposure. Includes Treasuries, agency securities, mortgage-backed securities, and corporate bonds.

Allowed option:
ID: DEVELOPED_EX_US
Name: Developed Markets ex-US
Symbol: VEA
Asset class: equity
Category: international_equity
Group: international_equity
Risk bucket: high
Description: Developed-market equity exposure outside the United States. Includes regions such as Europe, Japan, Canada, and developed Asia-Pacific markets.

Allowed option:
ID: EMERGING_MARKETS
Name: Emerging Markets
Symbol: VWO
Asset class: equity
Category: international_equity
Group: international_equity
Risk bucket: very_high
Description: Emerging-market equity exposure. Sensitive to global growth, currency moves, capital flows, commodity cycles, and country-specific policy risk.

Allowed option:
ID: EUROPE
Name: Europe Equities
Symbol: VGK
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: high
Description: European equity exposure. Sensitive to European growth, monetary policy, currency trends, energy costs, and regional earnings.

Allowed option:
ID: JAPAN
Name: Japan Equities
Symbol: EWJ
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: high
Description: Japanese equity exposure. Sensitive to Japanese corporate earnings, yen movements, monetary policy, and global trade conditions.

Allowed option:
ID: CHINA
Name: China Equities
Symbol: MCHI
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: very_high
Description: China equity exposure through publicly traded Chinese companies. Sensitive to Chinese growth, policy actions, currency moves, and geopolitical risk.

Allowed option:
ID: INDIA
Name: India Equities
Symbol: INDA
Asset class: equity
Category: regional_equity
Group: international_equity
Risk bucket: very_high
Description: Indian equity exposure. Sensitive to Indian economic growth, currency moves, domestic policy, valuations, and foreign capital flows.

Allowed option:
ID: GOLD
Name: Gold
Symbol: IAU
Asset class: commodity
Category: precious_metals
Group: commodities
Risk bucket: medium
Description: Gold exposure through a listed gold trust. Sensitive to real interest rates, US dollar strength, inflation expectations, and safe-haven demand.

Allowed option:
ID: BROAD_COMMODITIES
Name: Broad Commodities
Symbol: PDBC
Asset class: commodity
Category: broad_commodities
Group: commodities
Risk bucket: high
Description: Broad commodity exposure through a diversified commodity strategy ETF. Sensitive to energy, metals, agriculture, inflation expectations, and global demand.

Allowed option:
ID: SEMICONDUCTORS
Name: Semiconductors
Symbol: SMH
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: very_high
Description: Semiconductor equity exposure. Includes companies involved in chip design, manufacturing, equipment, and related supply chains.

Allowed option:
ID: SOFTWARE
Name: Software
Symbol: IGV
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: high
Description: Software equity exposure. Includes companies in application software, infrastructure software, and related technology services.

Allowed option:
ID: BROAD_AI_TECH
Name: Broad AI Technology
Symbol: AIQ
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: very_high
Description: Broad artificial intelligence and technology equity exposure. Includes companies associated with AI applications, infrastructure, data, and related technology services.

Allowed option:
ID: AUTONOMOUS_ROBOTICS
Name: Autonomous Technology and Robotics
Symbol: ARKQ
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: very_high
Description: Autonomous technology and robotics equity exposure. Includes companies associated with automation, robotics, autonomous transport, energy storage, and related technology platforms.

Allowed option:
ID: CYBERSECURITY
Name: Cybersecurity
Symbol: CIBR
Asset class: equity
Category: thematic_equity
Group: ai_and_technology
Risk bucket: high
Description: Cybersecurity equity exposure. Includes companies providing network security, identity, endpoint, cloud security, and related cybersecurity products and services.

Allowed option:
ID: SOLAR
Name: Solar Energy
Symbol: TAN
Asset class: equity
Category: thematic_equity
Group: clean_energy
Risk bucket: very_high
Description: Solar energy equity exposure. Includes companies associated with solar power equipment, development, installation, and related clean-energy supply chains.

Allowed option:
ID: METALS_MINING
Name: Metals and Mining
Symbol: XME
Asset class: equity
Category: commodity_equity
Group: commodities
Risk bucket: very_high
Description: Metals and mining equity exposure. Includes companies involved in steel, aluminum, precious metals, coal, copper, and diversified mining industries.

Allowed option:
ID: EQUAL_WEIGHT_SP500
Name: Equal-Weight S&P 500
Symbol: RSP
Asset class: equity
Category: broad_us_equity
Group: us_broad_market
Risk bucket: medium
Description: Equal-weight US large-cap equity exposure. Reduces concentration in the largest S&P 500 constituents compared with market-cap weighting.

Allowed option:
ID: BIOTECH
Name: Biotechnology
Symbol: XBI
Asset class: equity
Category: industry_equity
Group: healthcare_and_biotech
Risk bucket: very_high
Description: US biotechnology equity exposure. Sensitive to clinical data, financing conditions, regulation, mergers, and risk appetite.

Allowed option:
ID: REGIONAL_BANKS
Name: Regional Banks
Symbol: KRE
Asset class: equity
Category: industry_equity
Group: us_industry
Risk bucket: very_high
Description: US regional bank equity exposure. Sensitive to deposit trends, credit quality, yield curves, regulation, and commercial real estate conditions.

Allowed option:
ID: AEROSPACE_DEFENSE
Name: Aerospace and Defense
Symbol: ITA
Asset class: equity
Category: industry_equity
Group: us_industry
Risk bucket: high
Description: US aerospace and defense equity exposure. Sensitive to defense budgets, aircraft demand, supply chains, and geopolitical risk.

Allowed option:
ID: CANADA
Name: Canada Equities
Symbol: EWC
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: Canadian equity exposure through US-listed shares. Sensitive to financials, energy, materials, domestic growth, and Canadian dollar conditions.

Allowed option:
ID: UNITED_KINGDOM
Name: United Kingdom Equities
Symbol: EWU
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: United Kingdom equity exposure through US-listed shares. Sensitive to sterling, UK growth, global financials, energy, and dividend-oriented sectors.

Allowed option:
ID: AUSTRALIA
Name: Australia Equities
Symbol: EWA
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: Australian equity exposure through US-listed shares. Sensitive to banks, materials, commodity demand, China-linked growth, and Australian dollar conditions.

Allowed option:
ID: SOUTH_KOREA
Name: South Korea Equities
Symbol: EWY
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: South Korean equity exposure through US-listed shares. Sensitive to semiconductors, exports, won movements, global trade, and regional geopolitics.

Allowed option:
ID: TAIWAN
Name: Taiwan Equities
Symbol: EWT
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: Taiwan equity exposure through US-listed shares. Sensitive to semiconductor supply chains, global electronics demand, currency movements, and geopolitical risk.

Allowed option:
ID: BRAZIL
Name: Brazil Equities
Symbol: EWZ
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: Brazilian equity exposure through US-listed shares. Sensitive to commodities, rates, fiscal policy, currency moves, and emerging-market capital flows.

Allowed option:
ID: MEXICO
Name: Mexico Equities
Symbol: EWW
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: high
Description: Mexican equity exposure through US-listed shares. Sensitive to domestic growth, currency moves, trade links, remittances, and nearshoring activity.

Allowed option:
ID: SOUTH_AFRICA
Name: South Africa Equities
Symbol: EZA
Asset class: equity
Category: country_equity
Group: country_equity
Risk bucket: very_high
Description: South African equity exposure through US-listed shares. Sensitive to resources, domestic policy, currency moves, power availability, and emerging-market flows.

Allowed option:
ID: MORTGAGE_BACKED_BONDS
Name: Agency Mortgage-Backed Bonds
Symbol: MBB
Asset class: bond
Category: securitized_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: US agency mortgage-backed securities exposure. Sensitive to interest rates, prepayment behavior, mortgage spreads, and housing finance conditions.

Allowed option:
ID: MUNICIPAL_BONDS
Name: Municipal Bonds
Symbol: MUB
Asset class: bond
Category: municipal_bonds
Group: bonds_and_rates
Risk bucket: low
Description: US municipal bond exposure. Sensitive to rates, state and local credit conditions, fund flows, and tax-exempt fixed-income demand.

Allowed option:
ID: EMERGING_MARKET_BONDS
Name: Emerging Market USD Bonds
Symbol: EMB
Asset class: bond
Category: emerging_market_debt
Group: credit
Risk bucket: high
Description: US dollar emerging-market bond exposure. Sensitive to sovereign spreads, US rates, currency stress, commodity cycles, and global risk appetite.

Allowed option:
ID: INTERNATIONAL_BONDS
Name: International Aggregate Bonds
Symbol: BNDX
Asset class: bond
Category: international_bonds
Group: bonds_and_rates
Risk bucket: medium
Description: International investment-grade bond exposure. Sensitive to global rates, currency hedging, regional credit conditions, and non-US monetary policy.

Allowed option:
ID: SILVER
Name: Silver
Symbol: SLV
Asset class: commodity
Category: precious_metals
Group: commodities
Risk bucket: high
Description: Silver exposure through a listed trust. Sensitive to precious-metals demand, industrial usage, real rates, US dollar moves, and inflation expectations.

Allowed option:
ID: COPPER
Name: Copper
Symbol: CPER
Asset class: commodity
Category: industrial_metals
Group: commodities
Risk bucket: high
Description: Copper exposure through an exchange-traded product. Sensitive to industrial demand, China-linked growth, supply conditions, inventories, and electrification themes.

Allowed option:
ID: AGRICULTURE
Name: Agriculture Commodities
Symbol: DBA
Asset class: commodity
Category: agriculture
Group: commodities
Risk bucket: high
Description: Agricultural commodity exposure through a diversified exchange-traded product. Sensitive to weather, crop conditions, global demand, inventories, and currency moves.

Allowed option:
ID: OIL
Name: Crude Oil
Symbol: USO
Asset class: commodity
Category: energy_commodities
Group: commodities
Risk bucket: very_high
Description: Crude oil exposure through an exchange-traded product. Sensitive to supply, demand, inventories, OPEC policy, geopolitical risk, and futures-curve structure.

Allowed option:
ID: US_DOLLAR
Name: US Dollar
Symbol: UUP
Asset class: currency
Category: currency
Group: currencies
Risk bucket: medium
Description: US dollar currency exposure through an exchange-traded product. Sensitive to relative rates, global risk appetite, trade balances, and reserve-currency demand.

Allowed option:
ID: EURO
Name: Euro
Symbol: FXE
Asset class: currency
Category: currency
Group: currencies
Risk bucket: medium
Description: Euro currency exposure through an exchange-traded product. Sensitive to European rates, growth, fiscal policy, energy conditions, and US dollar movements.

Allowed option:
ID: YEN
Name: Japanese Yen
Symbol: FXY
Asset class: currency
Category: currency
Group: currencies
Risk bucket: high
Description: Japanese yen currency exposure through an exchange-traded product. Sensitive to Japanese monetary policy, rate differentials, carry trades, and safe-haven demand.

Allowed option:
ID: BITCOIN_ETF
Name: Bitcoin ETF
Symbol: IBIT
Asset class: crypto_proxy
Category: crypto_asset
Group: crypto_proxies
Risk bucket: very_high
Description: Bitcoin exposure through a US-listed spot bitcoin exchange-traded product. Sensitive to digital-asset flows, regulation, liquidity, rates, and risk appetite.

Allowed option:
ID: ETHEREUM_ETF
Name: Ethereum ETF
Symbol: ETHA
Asset class: crypto_proxy
Category: crypto_asset
Group: crypto_proxies
Risk bucket: very_high
Description: Ethereum exposure through a US-listed spot Ethereum exchange-traded product. Sensitive to digital-asset flows, network activity, regulation, liquidity, and risk appetite.
