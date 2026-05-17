# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make one-shot market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

Your objective is to allocate 100% across the allowed options you expect to produce the strongest risk-aware total return over the round horizon, using the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by the realized weighted return of its submitted portfolio relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official one-shot leaderboard.

Your portfolio is scored by the weighted realized percentage return over the round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

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

- Round ID: CB-2026-05-17-1M
- Decision date: 2026-05-17
- Research cutoff UTC: 2026-05-17T06:01:00Z
- Decision deadline UTC: 2026-05-18T01:00:00Z
- Horizon: one month
- Entry date: 2026-05-15
- Exit date: 2026-06-17
- Entry rule: Use Tiingo EOD adjusted close from the last trading close before the decision deadline; CASH return is 0 unless explicitly priced.
- Exit rule: Use Tiingo EOD adjusted close on the exit_date for each selected option; CASH return is 0 unless explicitly priced.
- Submission format: portfolio
- Scoring benchmark: S&P 500 / SPY
- Return calculation: adjusted close prices are used when available.
- Portfolio holdings allowed: 1-5
- Portfolio allocation increment: 5%
- Portfolio minimum allocation: 5%
- Portfolio total allocation: 100%

## Briefing

# **CapitalBench Briefing**

## **1\. Research Cutoff**

Sunday, May 17, 2026, at 2:01 AM America/Toronto.

## **2\. Fact-Only Statement**

This briefing contains factual inputs only. It does not rank, recommend, analyze, or map facts to CapitalBench options.

## **3\. Data Availability Notes**

| data area | status | factual note |
| :---- | :---- | :---- |
| Inflation | provided | Headline CPI, Core CPI, PCE, Core PCE |
| Labor market | provided | Unemployment rate, Nonfarm payrolls |
| Growth/activity | provided | GDP, ISM Manufacturing, ISM Services, Industrial production |
| Consumer | provided | Retail sales, UoM Consumer Sentiment |
| Housing | provided | Building permits, Housing starts, Case-Shiller index |
| Federal Reserve policy | provided | Fed funds rate, Dissenting votes, Chair confirmation |
| Treasury yields | provided | 10-year, 2-year, 30-year |
| Real rates | provided | 10-year TIPS yield |
| Breakeven inflation | provided | 10-year breakeven inflation rate |
| US dollar | provided | DXY index |
| Volatility | provided | VIX index |
| Credit spreads | provided | ICE BofA US High Yield OAS, CMBS OAS |
| Broad US equities | provided | Index values, YTD returns, P/E, Revenue/Margin tracking |
| US sectors | not provided | Factual sector performance data not provided in source reports |
| Bonds/rates | provided | Yield metrics |
| Credit | provided | Spread metrics |
| International equities | provided | Europe GDP/CPI, Japan CPI, China GDP, India GDP projections |
| Commodities | provided | Spot gold, WTI crude, Brent crude |
| AI/technology | provided | Semiconductor market projection, Hyperscaler capex projection |
| Scheduled calendar | provided | Macroeconomic release schedule, Trump-Xi summit dates |
| Source-reported uncertainties | provided | Identified source-reported uncertainties available |

## **4\. Macro Release Table**

| indicator | source-reported value | prior value | unit | release or observation date | period covered | status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Consumer Price Index (CPI) | \+0.6% MoM / 3.8% YoY | 3.3% YoY | % | May 12, 2026 | April 2026 | observed |
| Core CPI | \+0.4% MoM / 2.8% YoY | 2.6% YoY | % | May 12, 2026 | April 2026 | observed |
| PCE Price Index | 3.5% YoY | not provided in source reports | % | April 30, 2026 | March 2026 | observed |
| Core PCE Price Index | 3.2% YoY | not provided in source reports | % | April 30, 2026 | March 2026 | observed |
| Unemployment Rate | 4.3% | 4.3% | % | May 8, 2026 | April 2026 | observed |
| Nonfarm Payrolls | \+115,000 | not provided in source reports | jobs | May 8, 2026 | April 2026 | observed |
| Real GDP (Advance) | 2.0% SAAR | 0.5% SAAR | % | April 30, 2026 | Q1 2026 | observed |
| Retail Sales | \+0.5% MoM | \+1.6% MoM | % | May 14, 2026 | April 2026 | observed |
| ISM Manufacturing PMI | 52.7 | 52.7 | index | May 1, 2026 | April 2026 | observed |
| ISM Services PMI | 53.6 | not provided in source reports | index | May 5, 2026 | April 2026 | observed |
| ISM Services Prices Index | 70.7 | not provided in source reports | index | May 5, 2026 | April 2026 | observed |
| ISM Services New Orders | 53.5 | not provided in source reports | index | May 5, 2026 | April 2026 | observed |
| UoM Consumer Sentiment | 48.2 | 49.8 | index | May 8, 2026 | May 2026 (Preliminary) | observed |
| Industrial Production | \+0.7% MoM | not provided in source reports | % | May 15, 2026 | April 2026 | observed |
| Manufacturing Output | \+0.6% MoM | not provided in source reports | % | May 15, 2026 | April 2026 | observed |
| Capacity Utilization | 76.1% | not provided in source reports | % | May 15, 2026 | April 2026 | observed |
| Building Permits | 1,372,000 SAAR | not provided in source reports | units | April 29, 2026 | March 2026 | observed |
| Housing Starts | 1,502,000 SAAR | not provided in source reports | units | April 29, 2026 | March 2026 | observed |
| Case-Shiller Home Price Index | \+0.7% Annual | not provided in source reports | % | April 28, 2026 | February 2026 | observed |

## **5\. Federal Reserve, Rates, And Yields**

| item | source-reported value | prior value if provided | unit | release or observation date | period covered | status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Federal Funds Target Range | 3.50% \- 3.75% | not provided in source reports | % | April 29, 2026 | April 2026 | observed |
| FOMC Dissenting Votes | 4 | not provided in source reports | votes | April 29, 2026 | April 2026 | observed |
| 10-Year Treasury Note | 4.59% | not provided in source reports | % | May 15, 2026 | May 15, 2026 | observed |
| 2-Year Treasury Note | 4.09% | not provided in source reports | % | May 15, 2026 | May 15, 2026 | observed |
| 30-Year Treasury Bond | 5.11% | not provided in source reports | % | May 15, 2026 | May 15, 2026 | observed |
| 10-Year TIPS | 2.08% | not provided in source reports | % | May 15, 2026 | May 15, 2026 | observed |
| 10-Year Breakeven Inflation | 2.49% | not provided in source reports | % | May 15, 2026 | May 15, 2026 | observed |
| Implied Probability of 25bps Hike by Year-End | \>30% | virtually zero percent | % | May 15, 2026 | End of 2026 | estimate |

## **6\. Credit, Volatility, And Liquidity Measures**

| measure | source-reported value | prior value if provided | unit | observation date | period covered | status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Chicago Fed NFCI | \-0.52 | \-0.49 | index | May 8, 2026 | Week ending May 8, 2026 | observed |
| CBOE Volatility Index (VIX) | 18.43 | not provided in source reports | index | May 15, 2026 | May 15, 2026 | observed |
| ICE BofA US High Yield OAS | 2.76 | not provided in source reports | % | May 15, 2026 | May 14, 2026 | observed |
| Chicago Fed CMBS OAS Spread | \-3.46 | not provided in source reports | spread | May 8, 2026 | Week ending April 24, 2026 | observed |

## **7\. US Equity Observed Data**

| index / group / measure | source-reported value or return | period covered | observation date | status |
| :---- | :---- | :---- | :---- | :---- |
| S\&P 500 Index | 7,408.50 (+8.2% YTD, \-1.2% daily) | YTD | May 15, 2026 | observed |
| S\&P 500 Forward P/E Ratio | 21.07 | 12-Month Forward | May 15, 2026 | observed |
| S\&P 500 Blended Revenue Growth | 11.4% | Q1 2026 | May 15, 2026 | estimate |
| S\&P 500 Blended Net Profit Margin | 14.7% | Q1 2026 | May 15, 2026 | estimate |
| S\&P 500 Cap-Weighted Return | \+18.4% | Since March 30, 2026 | May 15, 2026 | observed |
| S\&P 500 Equal-Weighted Return | \+8.3% | Since March 30, 2026 | May 15, 2026 | observed |
| Nasdaq Composite | 26,225.14 (+12.8% YTD) | YTD | May 15, 2026 | observed |
| Russell 2000 | 2,793.30 (+12.5% YTD) | YTD | May 15, 2026 | observed |

## **8\. US Sector And Theme Observed Data**

| sector or theme | source-reported metric | source-reported value | period covered | observation date | status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Semiconductors | Projected Global Market Revenue | $1.29 trillion | 2026 Full Year | April 2026 | forecast |
| Semiconductors | Projected DRAM Revenue | $418.6 billion | 2026 Full Year | April 2026 | forecast |
| AI Infrastructure | US Hyperscaler AI Capital Expenditures | \>$600 billion | 2026 \- 2027 | May 2026 | forecast |

## **9\. Bonds And Credit Observed Data**

| asset area or measure | source-reported value | period covered | observation date | status |
| :---- | :---- | :---- | :---- | :---- |
| ICE BofA US High Yield OAS | 2.76% | May 14, 2026 | May 15, 2026 | observed |
| Chicago Fed CMBS OAS Spread | \-3.46 | Week ending April 24, 2026 | May 8, 2026 | observed |

## **10\. International Observed Data**

| region or country | source-reported metric | source-reported value | period covered | observation date | status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Europe | ECB Deposit Facility Rate | 2.00% | April 2026 | April 30, 2026 | observed |
| Europe | Euro Area Annual Inflation | 3.0% | April 2026 | April 30, 2026 | observed |
| Europe | Eurozone GDP Growth | 0.1% | Q1 2026 | April 30, 2026 | observed |
| Japan | Core CPI (excluding fresh food) | 3.1% YoY | not provided in source reports | May 17, 2026 | observed |
| Japan | Bank of Japan Policy Rate | 0.75% | not provided in source reports | May 17, 2026 | observed |
| Japan | Currency Market Interventions | 10 trillion yen | April 30 \- May 8, 2026 | May 9, 2026 | estimate |
| China | Real GDP Growth | 5.2% | Year-to-Date | May 17, 2026 | observed |
| China | Incremental Capital Output Ratio (ICOR) | 7.2 | not provided in source reports | May 14, 2026 | observed |
| India | Real GDP Growth | 7.5% | FY26 | May 11, 2026 | forecast |
| India | Real GDP Growth | 6.6% | FY27 | May 11, 2026 | forecast |

## **11\. Commodities And Currency Observed Data**

| commodity or currency measure | source-reported value | period covered | observation date | status |
| :---- | :---- | :---- | :---- | :---- |
| Spot Gold | $4,551.49 per ounce | May 15, 2026 | May 15, 2026 | observed |
| WTI Crude Oil | $105.42 per barrel | May 15, 2026 | May 15, 2026 | observed |
| Brent Crude Oil | $109.26 per barrel | May 15, 2026 | May 15, 2026 | observed |
| US Dollar Index (DXY) | 99.28 (+0.6% YTD) | YTD | May 15, 2026 | observed |

## **12\. Time-Stamped News And Policy Facts**

| date/time | event or announcement | entity involved | exact source-reported fact | status |
| :---- | :---- | :---- | :---- | :---- |
| April 29, 2026 | FOMC Meeting | Federal Open Market Committee | Four policymakers registered dissenting votes. | reported |
| May 13, 2026 | Fed Chair Confirmation | United States Senate | Kevin Warsh was confirmed by the United States Senate in a 54-45 vote to succeed Jerome Powell as Chair of the Federal Reserve. | observed |
| May 13-15, 2026 | Bilateral Summit | United States and China | United States President Donald Trump and Chinese President Xi Jinping held a bilateral summit in Beijing. | observed |

## **13\. Scheduled Calendar During The One-Month Window**

| date | scheduled event | entity or publisher | expected release type | forecast or consensus value if provided as of cutoff | status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| May 21, 2026 | Monthly State Retail Sales | Census Bureau | Data release | not provided in source reports | scheduled |
| May 28, 2026 | Q1 GDP (2nd Estimate) | BEA | Data release | not provided in source reports | scheduled |
| May 28, 2026 | PCE Price Index (April) | BEA | Data release | not provided in source reports | scheduled |
| June 5, 2026 | Employment Situation (Jobs) | BLS | Data release | not provided in source reports | scheduled |
| June 7, 2026 | Q4 FY26 GDP Release | India MoSPI | Data release | not provided in source reports | scheduled |
| June 10, 2026 | CPI Release (May) | BLS | Data release | not provided in source reports | scheduled |
| June 11, 2026 | PPI Release (May) | BLS | Data release | not provided in source reports | scheduled |
| June 17, 2026 | FOMC Policy Decision | Federal Reserve | Policy statement / Projections | not provided in source reports | scheduled |

## **14\. Source-Reported Uncertainties**

| uncertainty | source-reported wording or concise factual paraphrase | source date | status |
| :---- | :---- | :---- | :---- |
| Fed Leadership Transition Impact | Reaction function of incoming Chair Kevin Warsh to current inflation spike given his views on AI productivity. | May 17, 2026 | source\_reported\_uncertainty |
| Strait of Hormuz Disruption | Duration and severity of the disruption, and the extent to which it will impact baseline inflation forecasts throughout 2026\. | May 17, 2026 | source\_reported\_uncertainty |
| June 2026 FOMC Projections | Trajectory of the "dot plot" and whether median policymaker projects further interest rate hikes. | May 17, 2026 | source\_reported\_uncertainty |
| Q2 2026 GDP and Earnings Realities | Extent to which 4.5%+ yields and 20%+ higher gasoline prices have degraded consumer demand and corporate profit margins prior to July reporting. | May 17, 2026 | source\_reported\_uncertainty |
| Japanese Currency Intervention | Exact scale, efficacy, and Bank of Japan's ultimate threshold for further yen depreciation before rate hikes. | May 17, 2026 | source\_reported\_uncertainty |

## **15\. Missing Or Not-Provided Data**

| data area | missing item | note |
| :---- | :---- | :---- |
| US sectors | Quantitative sector performance metrics | not provided in source reports |
| Credit | Specific corporate bond performance returns | not provided in source reports |
| Commodities | Specific agricultural/industrial raw material index values | not provided in source reports |
| International equities | Exact quantitative magnitude of Bank of Japan intervention | not provided in source reports |

## **16\. Final Neutrality Statement**

This briefing contains factual inputs only. It does not rank, recommend, analyze, or map facts to CapitalBench options.

## Full-Universe Trailing Returns

This table is mechanically calculated from Tiingo EOD adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

- Source: tiingo_eod_adj_close
- As-of date requested: 2026-05-17
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-05-17 | 0.00% | 0.00% | 0.00% | 0.00% | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-05-15 | 0.08% | 0.27% | 1.79% | 3.90% | pass |
| SP500 | SPY | us_broad_market | 2026-05-15 | 0.21% | 4.09% | 11.68% | 25.82% | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-05-15 | -0.04% | 3.48% | 11.79% | 25.45% | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-05-15 | -0.32% | 9.26% | 17.74% | 36.59% | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-05-15 | 0.67% | 4.42% | 6.84% | 24.42% | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-05-15 | -0.74% | 2.21% | 15.61% | 23.65% | pass |
| MID_CAP | IJH | us_size_factor | 2026-05-15 | -2.39% | -0.93% | 15.45% | 18.43% | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-05-15 | -2.31% | 0.66% | 19.88% | 33.71% | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-05-15 | -2.67% | -0.23% | 21.55% | 35.28% | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-05-15 | 0.32% | 2.16% | 19.67% | 23.85% | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-05-15 | -0.40% | -2.96% | 1.80% | 0.29% | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-05-15 | -1.17% | 8.68% | 23.00% | 30.35% | pass |
| TECHNOLOGY | XLK | us_sector | 2026-05-15 | 0.42% | 14.20% | 24.62% | 50.93% | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-05-15 | -0.74% | -2.54% | 5.08% | 15.46% | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-05-15 | -3.05% | -3.22% | 2.30% | 7.91% | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-05-15 | 0.55% | 2.64% | 11.76% | 5.98% | pass |
| HEALTHCARE | XLV | us_sector | 2026-05-15 | 1.12% | -2.49% | -3.55% | 10.96% | pass |
| FINANCIALS | XLF | us_sector | 2026-05-15 | -0.27% | -2.54% | 0.17% | 0.57% | pass |
| INDUSTRIALS | XLI | us_sector | 2026-05-15 | -1.04% | -1.22% | 14.57% | 20.80% | pass |
| ENERGY | XLE | us_sector | 2026-05-15 | 6.71% | 8.03% | 33.56% | 43.55% | pass |
| MATERIALS | XLB | us_sector | 2026-05-15 | -2.50% | -3.05% | 18.85% | 17.81% | pass |
| UTILITIES | XLU | us_sector | 2026-05-15 | -1.90% | -4.96% | -0.62% | 9.78% | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-05-15 | -2.66% | -2.81% | 8.14% | 6.45% | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-05-15 | -1.53% | -2.20% | -1.29% | 3.38% | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-05-15 | -2.81% | -3.56% | -3.97% | 1.35% | pass |
| TIPS | TIP | bonds_and_rates | 2026-05-15 | -0.71% | -0.28% | 0.96% | 4.50% | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-05-15 | -1.23% | -1.60% | 0.03% | 5.35% | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-05-15 | -0.85% | -0.96% | 2.16% | 6.05% | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-05-15 | -1.17% | -1.51% | -0.05% | 4.40% | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-05-15 | -2.47% | -0.79% | 16.25% | 30.77% | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-05-15 | -3.47% | -1.25% | 9.88% | 25.83% | pass |
| EUROPE | VGK | international_equity | 2026-05-15 | -2.64% | -3.68% | 8.67% | 17.58% | pass |
| JAPAN | EWJ | international_equity | 2026-05-15 | -1.25% | 0.98% | 14.61% | 31.44% | pass |
| CHINA | MCHI | international_equity | 2026-05-15 | -2.88% | -4.47% | -8.67% | 6.39% | pass |
| INDIA | INDA | international_equity | 2026-05-15 | -3.71% | -6.42% | -12.19% | -12.20% | pass |
| GOLD | IAU | commodities | 2026-05-15 | -3.78% | -6.38% | 12.35% | 42.04% | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-05-15 | 2.99% | 10.51% | 41.67% | 51.67% | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-05-15 | -1.80% | 19.86% | 63.99% | 126.46% | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-05-15 | 0.69% | 7.87% | -13.00% | -12.72% | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-05-15 | -1.24% | -0.79% | 9.92% | 13.85% | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-05-15 | -2.98% | -5.75% | 14.18% | 65.98% | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-05-15 | -4.12% | -4.83% | 15.59% | 15.89% | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-05-15 | -2.78% | -6.32% | 6.67% | 27.04% | pass |
| CANADA | EWC | country_equity | 2026-05-15 | -1.12% | -1.85% | 15.13% | 32.93% | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-05-15 | -2.42% | -5.55% | 9.46% | 21.86% | pass |
| AUSTRALIA | EWA | country_equity | 2026-05-15 | -2.78% | -4.93% | 13.94% | 16.44% | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-05-15 | -5.96% | 17.42% | 96.66% | 211.16% | pass |
| TAIWAN | EWT | country_equity | 2026-05-15 | -5.03% | 9.69% | 51.18% | 76.79% | pass |
| BRAZIL | EWZ | country_equity | 2026-05-15 | -7.39% | -11.98% | 14.49% | 36.48% | pass |
| MEXICO | EWW | country_equity | 2026-05-15 | -3.33% | -2.83% | 19.49% | 34.66% | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-05-15 | -6.05% | -9.73% | 7.46% | 40.32% | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-05-15 | -1.41% | -1.73% | 0.59% | 5.69% | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-05-15 | -0.82% | -0.90% | 0.69% | 4.84% | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-05-15 | -1.50% | -1.61% | 1.21% | 10.21% | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-05-15 | -1.18% | -1.34% | -0.88% | 1.30% | pass |
| SILVER | SLV | commodities | 2026-05-15 | -5.44% | -6.23% | 51.84% | 135.63% | pass |
| COPPER | CPER | commodities | 2026-05-15 | -0.34% | 2.28% | 23.39% | 33.31% | pass |
| AGRICULTURE | DBA | commodities | 2026-05-15 | -0.50% | 3.38% | 9.07% | 5.44% | pass |
| OIL | USO | commodities | 2026-05-15 | 10.96% | 27.74% | 107.90% | 117.67% | pass |
| US_DOLLAR | UUP | currencies | 2026-05-15 | 1.57% | 1.50% | 1.92% | 3.02% | pass |
| EURO | FXE | currencies | 2026-05-15 | -1.34% | -1.23% | 0.67% | 5.04% | pass |
| YEN | FXY | currencies | 2026-05-15 | -1.28% | -0.07% | -2.35% | -8.35% | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-05-15 | -1.39% | 2.00% | -13.97% | -24.29% | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-05-15 | -4.12% | -8.81% | -26.20% | -14.71% | pass |

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
