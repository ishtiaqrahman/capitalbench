# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make saved market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-week outcome window resolves.

The scoring timeline is central to the task: the portfolio is measured from the adjusted close on the entry date to the adjusted close on the exit date, calculated after regular trading ends on the exit date. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that exit close.

Optimize only for the portfolio you expect to perform best over this close-to-close one-week scoring window. Use longer-horizon facts only when they are likely to affect prices before the exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical price-context table. Treat inclusion, section order, grouping, row count, and price-context table order as context, not recommendation signals.

Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to allocate to an option. When recent performance matters to a holding, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close.

Your objective is to allocate 100% across the allowed options to maximize expected one-week realized portfolio return, measured from the entry date to the exit date, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official leaderboard.

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
- If a holding rationale cites momentum, recent returns, or trailing performance, do not present price history alone as independent evidence. Mention any independent support present in the briefing, or state that support is limited, and include the relevant reversal or positioning risk in key_risks.
- key_risks must be a list of 2-5 concrete risks that could cause the portfolio to underperform; do not only list generic market risk.
- Do not provide a ranked list, backup portfolio, second-best portfolio, or alternative recommendation.
- Do not include financial-advice disclaimers. This is a benchmark response, not advice to a person.
- The JSON object must contain no extra fields.

## Round Metadata

- Round ID: CB-2026-06-25-1W
- Decision date: 2026-06-25
- Research cutoff UTC: 2026-06-25T23:00:00Z
- Decision deadline UTC: 2026-06-26T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-25
- Exit date: 2026-07-02
- Scoring window: 2026-06-25 to 2026-07-02; optimize for this one week window only.
- Close-to-close scoring: the entry price is the adjusted close on the entry date, and the exit price is the adjusted close on the exit date after regular trading ends.
- Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.
- Input-bias control: treat fact inclusion, section order, grouping, and price-context table order as context, not recommendations; do not infer expected return from mention count or placement.
- Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to select or allocate to an option.
- Continuation evidence: when a holding or selection relies on recent price strength, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close. Do not invent support that is not in the input.
- Entry rule: Use adjusted close prices on Thursday, June 25, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, July 2, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Submission format: portfolio
- Scoring benchmark: S&P 500 / SPY
- Return calculation: adjusted close prices are used when available.
- Portfolio holdings allowed: 1-5
- Portfolio allocation increment: 5%
- Portfolio minimum allocation: 5%
- Portfolio total allocation: 100%

## Briefing

# CapitalBench Briefing

Research cutoff: 2026-06-25T23:00:00Z.

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. A mechanical full-universe price, risk, and benchmark-relative appendix follows this briefing in the model input.

## U.S. Market Close

- On June 25, 2026, the S&P 500 closed at 7,357.49, down 0.73 points, or less than 0.1%. The Dow Jones Industrial Average closed at 51,920.62, up 71.72 points, or 0.1%. The Nasdaq Composite closed at 25,358.60, down 118.03 points, or 0.5%. The Russell 2000 closed at 3,007.86, up 21.23 points, or 0.7%.
- Through the June 25 close, week-to-date index moves were: S&P 500 down 1.9%, Dow up 0.7%, Nasdaq down 4.4%, Russell 2000 up 0.9%.
- Through the June 25 close, year-to-date index moves were: S&P 500 up 7.5%, Dow up 8.0%, Nasdaq up 9.1%, Russell 2000 up 21.2%.

## U.S. Macro Data

- May 2026 personal income increased $181.6 billion, or 0.7% month over month. Disposable personal income increased $164.9 billion, or 0.7%. Personal consumption expenditures increased $156.1 billion, or 0.7%.
- May 2026 real disposable personal income increased 0.3%. The personal saving rate was 3.0%.
- May 2026 PCE prices were up 4.1% from a year earlier. PCE prices excluding food and energy were up 3.4% from a year earlier.
- Q1 2026 real GDP increased at a 2.1% annual rate in the third estimate, compared with a 0.5% increase in Q4 2025. The third estimate revised real GDP up 0.5 percentage point from the prior estimate.
- Q1 2026 real GDI increased 1.2%. The average of real GDP and real GDI increased 1.7%.
- Q1 2026 profits from current production increased $74.4 billion.
- Initial unemployment claims were 215,000 for the week ending June 20, 2026, down 12,000 from the revised prior-week level of 227,000. The four-week moving average was 224,250, up 750 from the prior revised average.
- May 2026 manufactured durable-goods new orders decreased $15.6 billion, or 4.5%, to $332.1 billion after an 8.5% April increase. Excluding transportation, new orders increased 1.3%; excluding defense, new orders decreased 4.6%.
- May 2026 durable-goods shipments increased $3.2 billion, or 1.0%, to $327.9 billion. Unfilled orders increased $9.2 billion, or 0.6%, to $1,579.5 billion. Inventories increased $0.9 billion, or 0.2%, to $600.0 billion.
- May 2026 CPI rose 0.5% month over month and 4.2% year over year. CPI excluding food and energy rose 0.2% month over month and 2.9% year over year.
- May 2026 PPI for final demand rose 1.1% month over month and 6.5% year over year. Final demand excluding foods, energy, and trade services rose 0.8% month over month and 5.1% year over year.
- May 2026 nonfarm payroll employment rose by 172,000 and the unemployment rate was 4.3%.

## Rates And Policy Calendar

- The Federal Reserve's June 25 H.15 release showed latest available Treasury constant maturity observations for June 24, 2026: 2-year 4.11%, 5-year 4.17%, 10-year 4.41%, 20-year 4.87%, and 30-year 4.86%. The effective federal funds rate was 3.63% and the bank prime loan rate was 6.75%.
- On June 17, 2026, the FOMC maintained the target range for the federal funds rate at 3.50% to 3.75%.
- The next scheduled FOMC meeting is July 28-29, 2026. Minutes from the June 16-17 meeting are scheduled for July 8, 2026 at 2:00 PM ET.

## Energy, Commodities, And Crypto

- For the week ending June 19, 2026, U.S. commercial crude oil inventories excluding the Strategic Petroleum Reserve decreased by 6.1 million barrels to 412.1 million barrels, about 7% below the five-year average.
- Gasoline inventories increased by 2.1 million barrels and were 5% below the five-year average. Distillate inventories increased by 3.1 million barrels and were 10% below the five-year average.
- U.S. crude refinery inputs averaged 17.1 million barrels per day for the week ending June 19, down 81,000 barrels per day from the prior week. Refineries operated at 96.1% capacity utilization.
- On June 25, front-month Comex gold futures rose 1.01% to $4,030.50 per ounce and silver rose 0.51% to $58.348 per ounce.
- Bitcoin was quoted at $59,860 at 5:53 PM EDT on June 25, 2026, up 1.11% from the previous close. The displayed 52-week range was $58,065 to $126,273.

## Business Activity And Global Data

- The June 2026 flash U.S. Composite Output PMI was 52.2, up from 51.5 in May. The flash U.S. Manufacturing PMI was 55.7, up from 55.1 and a 49-month high. The flash U.S. Services Business Activity Index was 51.3, up from 50.7 and a four-month high. The release also reported lower employment and elevated price inflation.
- The Eurozone flash composite PMI rose from 48.5 in May to 49.5 in June and remained below 50.0.
- Japan's flash composite output PMI rose from 51.1 in May to 52.5 in June.
- HSBC/S&P Global flash India PMI data indicated robust but softer growth in June, slower demand growth, a softer expansion in employment, receding inflation pressures, and downgraded growth forecasts among survey participants.

## Company And Sector Facts

- Micron reported fiscal Q3 2026 revenue of $41.46 billion, compared with $23.86 billion in the prior quarter and $9.30 billion in the year-earlier quarter.
- Micron reported fiscal Q3 2026 GAAP net income of $28.24 billion, or $24.67 per diluted share, and non-GAAP net income of $28.86 billion, or $25.11 per diluted share.
- Micron guided fiscal Q4 2026 revenue to $50.0 billion plus or minus $1.0 billion, gross margin around 86%, and non-GAAP diluted EPS of $31.00 plus or minus $1.00.
- Micron said HBM4 built on 1-beta DRAM technology was in high-volume shipments for its lead customer's platform; HBM4E development was underway with volume production expected in calendar 2027.

## Scheduled Dates

- The June 2026 Employment Situation is scheduled for July 2, 2026 at 8:30 AM ET.
- The full May manufacturers' shipments, inventories, and orders report is scheduled for July 2, 2026 at 10:00 AM ET.
- Friday, July 3, 2026 is the observed Independence Day market holiday on the NYSE calendar.
- U.S. international trade in goods and services for May 2026 is scheduled for July 7, 2026.
- June FOMC minutes are scheduled for July 8, 2026 at 2:00 PM ET.
- June 2026 CPI and Real Earnings are scheduled for July 14, 2026 at 8:30 AM ET.
- June 2026 PPI is scheduled for July 15, 2026 at 8:30 AM ET.
- June 2026 import and export prices are scheduled for July 17, 2026 at 8:30 AM ET.
- State employment and unemployment for June 2026 and usual weekly earnings for Q2 2026 are scheduled for July 21, 2026 at 10:00 AM ET.
- The advance June durable-goods report is scheduled for July 27, 2026.
- The next FOMC meeting is scheduled for July 28-29, 2026.
- June 2026 personal income and outlays and the Q2 2026 GDP advance estimate are scheduled for July 30, 2026 at 8:30 AM ET.

## Measurement Notes

- GDP and PCE releases are estimates and are subject to scheduled revisions.
- Durable-goods data are advance estimates; the full May report is scheduled for July 2, 2026.
- Weekly claims data are advance readings and prior weeks may be revised.
- Flash PMI readings are preliminary and based on most, but not all, monthly survey responses.
- Federal Reserve H.15 daily Treasury observations in the June 25 release carried latest available table observations through June 24.

## Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close
- As-of date requested: 2026-06-25
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-25 | 0.00% | 0.00% | 0.00% | 0.00% | 1.92% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-25 | 0.03% | 0.28% | 1.75% | 3.85% | 2.20% | 0.23% | -0.01% | 76.19% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-06-25 | -1.67% | -1.92% | 6.93% | 22.28% | 0.00% | 16.55% | -4.49% | 52.38% | -3.08% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-25 | -1.62% | -1.48% | 7.43% | 23.02% | 0.44% | 16.80% | -4.36% | 52.38% | -2.77% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-25 | -3.17% | -1.80% | 15.09% | 33.01% | 0.13% | 31.09% | -7.03% | 47.62% | -3.89% | 1.35 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-25 | -4.13% | -5.94% | -1.51% | 14.13% | -4.01% | 21.08% | -8.21% | 47.62% | -8.21% | 1.23 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-25 | 0.92% | 2.88% | 15.79% | 29.73% | 4.81% | 14.70% | -2.40% | 57.14% | 0.00% | 0.76 | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-25 | 0.90% | 2.68% | 14.12% | 26.90% | 4.60% | 15.84% | -2.40% | 61.90% | 0.00% | 1.02 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-25 | 1.12% | 3.13% | 18.77% | 42.48% | 5.06% | 21.82% | -3.55% | 57.14% | 0.00% | 1.30 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-25 | 1.49% | 2.89% | 19.65% | 44.29% | 4.82% | 17.64% | -2.75% | 57.14% | 0.00% | 1.07 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-25 | 1.11% | -1.39% | 17.45% | 26.44% | 0.53% | 10.79% | -2.93% | 42.86% | -1.87% | 0.33 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-25 | 2.67% | 1.57% | 5.33% | 6.66% | 3.49% | 14.77% | -3.48% | 57.14% | -2.57% | 0.09 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-25 | 0.23% | 8.16% | 33.07% | 45.28% | 10.08% | 42.03% | -7.46% | 61.90% | -1.71% | 1.45 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-25 | -3.47% | -0.19% | 26.46% | 48.81% | 1.73% | 42.03% | -10.89% | 52.38% | -6.77% | 1.64 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-25 | -3.28% | -8.39% | -10.07% | 1.62% | -6.46% | 16.11% | -9.27% | 42.86% | -11.56% | 0.71 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-25 | -3.06% | -4.91% | -7.17% | 7.23% | -2.99% | 23.21% | -7.02% | 47.62% | -8.61% | 1.19 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-25 | 1.47% | 1.07% | 8.81% | 7.53% | 2.99% | 17.43% | -3.57% | 42.86% | -5.57% | -0.01 | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-25 | 4.63% | 5.25% | 0.74% | 18.25% | 7.17% | 18.27% | -3.34% | 57.14% | -2.03% | 0.40 | pass |
| FINANCIALS | XLF | us_sector | 2026-06-25 | 0.12% | 3.44% | -3.27% | 5.57% | 5.37% | 14.59% | -1.89% | 52.38% | -4.41% | 0.68 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-25 | 2.02% | 5.89% | 17.51% | 29.69% | 7.81% | 22.40% | -3.69% | 52.38% | 0.00% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-06-25 | 1.31% | -5.83% | 23.57% | 31.92% | -3.91% | 23.61% | -8.48% | 47.62% | -12.92% | -0.14 | pass |
| MATERIALS | XLB | us_sector | 2026-06-25 | 0.43% | 2.05% | 14.01% | 21.58% | 3.97% | 21.32% | -3.93% | 57.14% | -2.53% | 0.81 | pass |
| UTILITIES | XLU | us_sector | 2026-06-25 | 3.09% | 1.79% | 8.53% | 17.07% | 3.71% | 18.22% | -4.92% | 66.67% | -2.66% | 0.21 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-25 | 2.54% | 0.60% | 11.96% | 11.85% | 2.52% | 18.51% | -3.31% | 52.38% | -0.85% | 0.35 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-25 | 0.46% | 0.88% | -0.02% | 3.34% | 2.80% | 5.16% | -0.86% | 61.90% | -2.01% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-25 | 0.69% | 3.05% | 1.11% | 4.38% | 4.97% | 8.60% | -1.20% | 61.90% | -2.37% | 0.14 | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-25 | 0.10% | -0.04% | 1.15% | 3.72% | 1.88% | 4.26% | -0.98% | 57.14% | -0.56% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-25 | 0.39% | 1.04% | 0.85% | 5.30% | 2.96% | 4.98% | -0.81% | 52.38% | -0.48% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-25 | -0.16% | 0.14% | 1.56% | 5.68% | 2.06% | 3.75% | -0.59% | 47.62% | -0.20% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-25 | 0.35% | 0.87% | 0.88% | 4.48% | 2.80% | 4.04% | -0.57% | 61.90% | -0.82% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-25 | -1.59% | -0.35% | 14.32% | 31.04% | 1.57% | 23.94% | -4.85% | 61.90% | -1.70% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-25 | -3.24% | -2.26% | 9.67% | 22.83% | -0.34% | 24.31% | -5.67% | 47.62% | -3.98% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-06-25 | -0.50% | -0.51% | 6.83% | 19.18% | 1.41% | 17.12% | -3.12% | 47.62% | -1.15% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-06-25 | -2.98% | 1.06% | 15.91% | 34.51% | 2.98% | 27.40% | -5.14% | 66.67% | -3.69% | 1.17 | pass |
| CHINA | MCHI | international_equity | 2026-06-25 | -3.77% | -8.89% | -15.67% | -6.82% | -6.97% | 20.95% | -10.62% | 38.10% | -22.76% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-06-25 | -0.30% | 1.81% | -8.48% | -10.13% | 3.73% | 16.14% | -3.04% | 52.38% | -11.51% | 0.63 | pass |
| GOLD | IAU | commodities | 2026-06-25 | -4.56% | -10.73% | -10.23% | 20.46% | -8.81% | 29.69% | -12.28% | 47.62% | -25.46% | 0.66 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-25 | -2.36% | -10.05% | 20.04% | 28.18% | -8.13% | 18.78% | -12.58% | 33.33% | -14.81% | -0.17 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-25 | -3.49% | 5.77% | 74.89% | 132.14% | 7.69% | 64.40% | -10.69% | 57.14% | -4.79% | 2.21 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-25 | -4.86% | -9.86% | -21.67% | -21.34% | -7.94% | 44.20% | -21.29% | 23.81% | -28.03% | 1.21 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-25 | -3.92% | -1.56% | 24.85% | 49.28% | 0.36% | 50.06% | -12.52% | 57.14% | -8.50% | 1.83 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-25 | -7.01% | -11.33% | 3.92% | 44.97% | -9.41% | 42.73% | -13.89% | 38.10% | -13.89% | 2.14 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-25 | -0.96% | -0.89% | 15.14% | 13.15% | 1.04% | 41.20% | -11.74% | 38.10% | -11.23% | 1.08 | pass |
| SOLAR | TAN | clean_energy | 2026-06-25 | -4.47% | -16.08% | 13.78% | 72.90% | -14.16% | 53.06% | -21.72% | 42.86% | -21.72% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-06-25 | -7.01% | -11.28% | 0.94% | 66.54% | -9.36% | 46.77% | -19.22% | 42.86% | -18.08% | 1.73 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-25 | 1.24% | 2.37% | 10.15% | 20.33% | 4.29% | 12.47% | -2.04% | 61.90% | -0.15% | 0.75 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-25 | 7.83% | 13.79% | 20.14% | 82.86% | 15.71% | 34.33% | -6.53% | 71.43% | 0.00% | 1.07 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-25 | 4.86% | 6.97% | 13.34% | 31.71% | 8.90% | 22.05% | -3.44% | 71.43% | 0.00% | 0.86 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-25 | -0.67% | 3.51% | 7.95% | 31.06% | 5.43% | 29.00% | -4.54% | 52.38% | -5.14% | 1.02 | pass |
| CANADA | EWC | country_equity | 2026-06-25 | -0.43% | -1.38% | 6.02% | 28.88% | 0.54% | 15.22% | -3.20% | 52.38% | -2.64% | 0.81 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-25 | 0.92% | -1.85% | 5.58% | 20.79% | 0.07% | 14.15% | -3.40% | 38.10% | -4.39% | 0.74 | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-25 | -2.21% | -2.16% | 6.49% | 10.69% | -0.24% | 19.54% | -4.78% | 42.86% | -6.39% | 0.95 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-25 | -6.48% | 2.17% | 116.70% | 189.71% | 4.09% | 95.11% | -19.16% | 38.10% | -6.48% | 2.59 | pass |
| TAIWAN | EWT | country_equity | 2026-06-25 | -4.62% | 2.71% | 67.78% | 91.49% | 4.63% | 47.37% | -8.51% | 61.90% | -5.94% | 1.66 | pass |
| BRAZIL | EWZ | country_equity | 2026-06-25 | 1.33% | -5.44% | 9.73% | 29.65% | -3.52% | 20.77% | -7.67% | 33.33% | -17.31% | 1.03 | pass |
| MEXICO | EWW | country_equity | 2026-06-25 | -2.33% | -2.82% | 8.01% | 30.91% | -0.90% | 24.47% | -6.47% | 38.10% | -5.66% | 0.93 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-25 | -5.35% | -7.60% | -7.74% | 28.67% | -5.67% | 37.23% | -9.51% | 52.38% | -20.95% | 1.60 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-25 | 0.47% | 0.98% | 1.23% | 5.88% | 2.90% | 4.54% | -0.80% | 66.67% | -0.67% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-25 | 0.23% | 1.14% | 1.92% | 6.60% | 3.06% | 2.33% | -0.35% | 57.14% | -0.17% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-25 | -0.18% | 1.39% | 2.21% | 10.56% | 3.31% | 6.06% | -1.02% | 52.38% | -0.18% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-25 | 0.29% | 0.78% | 1.29% | 2.53% | 2.70% | 3.24% | -0.65% | 57.14% | -0.54% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-06-25 | -12.01% | -24.90% | -19.72% | 58.62% | -22.98% | 52.76% | -25.73% | 38.10% | -50.42% | 1.69 | pass |
| COPPER | CPER | commodities | 2026-06-25 | -4.84% | -5.25% | 8.13% | 19.83% | -3.33% | 33.89% | -10.57% | 52.38% | -8.92% | 1.26 | pass |
| AGRICULTURE | DBA | commodities | 2026-06-25 | 1.09% | -2.00% | 4.95% | 6.92% | -0.08% | 10.46% | -4.86% | 33.33% | -6.30% | 0.07 | pass |
| OIL | USO | commodities | 2026-06-25 | -4.84% | -20.21% | 55.71% | 49.11% | -18.29% | 44.25% | -24.54% | 33.33% | -28.54% | -1.03 | pass |
| US_DOLLAR | UUP | currencies | 2026-06-25 | 0.64% | 2.63% | 5.68% | 8.78% | 4.55% | 4.80% | -0.43% | 52.38% | -0.18% | -0.13 | pass |
| EURO | FXE | currencies | 2026-06-25 | -0.78% | -2.19% | -3.08% | -1.80% | -0.26% | 5.34% | -2.66% | 47.62% | -5.25% | 0.13 | pass |
| YEN | FXY | currencies | 2026-06-25 | -0.28% | -1.63% | -3.88% | -10.60% | 0.29% | 2.75% | -1.67% | 19.05% | -11.60% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-25 | -5.90% | -22.03% | -32.23% | -45.30% | -20.11% | 46.38% | -22.03% | 23.81% | -52.98% | 1.83 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-25 | -8.85% | -24.84% | -47.05% | -36.20% | -22.92% | 68.95% | -24.84% | 23.81% | -67.91% | 3.00 | pass |

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
