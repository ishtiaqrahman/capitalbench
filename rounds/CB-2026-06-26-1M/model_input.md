# CapitalBench Task

You are participating in an offline, time-resolved CapitalBench evaluation round.

CapitalBench evaluates how state-of-the-art language models make saved market allocation decisions from the same frozen information set. Your response will be compared against other participating models after the one-month outcome window resolves.

The scoring timeline is central to the task: the portfolio is measured from the adjusted close on the entry date to the adjusted close on the exit date, calculated after regular trading ends on the exit date. Optimize for facts, catalysts, positioning, liquidity, and risks that can plausibly affect prices before that exit close.

Optimize only for the portfolio you expect to perform best over this close-to-close one-month scoring window. Use longer-horizon facts only when they are likely to affect prices before the exit close.

Briefing-bias discipline: the briefing may group facts by broad asset area and include a mechanical price-context table. Treat inclusion, section order, grouping, row count, and price-context table order as context, not recommendation signals.

Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to allocate to an option. When recent performance matters to a holding, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close.

Your objective is to allocate 100% across the allowed options to maximize expected one-month realized portfolio return, measured from the entry date to the exit date, relative to the S&P 500 benchmark. Use the briefing, option list, and any included market-data table as the common information set. The official leaderboard ranks each model by realized weighted portfolio return relative to the S&P 500 benchmark. Multi-shot stability analysis, if run, is reported separately and does not change the official leaderboard.

Your portfolio is scored by the weighted realized percentage return over the one-month round window. Alpha is portfolio return minus S&P 500 return. Returns are calculated from adjusted close prices when available.

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

- Round ID: CB-2026-06-26-1M
- Decision date: 2026-06-26
- Research cutoff UTC: 2026-06-27T02:25:00Z
- Decision deadline UTC: 2026-06-27T03:30:00Z
- Horizon: one month
- Entry date: 2026-06-26
- Exit date: 2026-07-24
- Scoring window: 2026-06-26 to 2026-07-24; optimize for this one month window only.
- Close-to-close scoring: the entry price is the adjusted close on the entry date, and the exit price is the adjusted close on the exit date after regular trading ends.
- Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.
- Input-bias control: treat fact inclusion, section order, grouping, and price-context table order as context, not recommendations; do not infer expected return from mention count or placement.
- Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to select or allocate to an option.
- Continuation evidence: when a holding or selection relies on recent price strength, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close. Do not invent support that is not in the input.
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Submission format: portfolio
- Scoring benchmark: S&P 500 / SPY
- Return calculation: adjusted close prices are used when available.
- Portfolio holdings allowed: 1-5
- Portfolio allocation increment: 5%
- Portfolio minimum allocation: 5%
- Portfolio total allocation: 100%

## Briefing

# CapitalBench Briefing

Research cutoff: 2026-06-27T02:25:00Z.

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. A mechanical full-universe price, risk, and benchmark-relative appendix follows this briefing in the model input.

## U.S. Market Close

- On June 26, 2026, the S&P 500 closed at 7,354.02, down 3.47 points, or less than 0.1%. The Dow Jones Industrial Average closed at 51,876.11, down 44.51 points, or 0.1%. The Nasdaq Composite closed at 25,297.62, down 60.99 points, or 0.2%. The Russell 2000 closed at 3,010.08, up 2.23 points, or 0.1%.
- For the week ending June 26, 2026, the S&P 500 was down 2.0%, the Dow was up 0.6%, the Nasdaq was down 4.6%, and the Russell 2000 was up 1.0%.
- Through the June 26 close, year-to-date index moves were: S&P 500 up 7.4%, Dow up 7.9%, Nasdaq up 8.8%, Russell 2000 up 21.3%.
- On June 26, nearly two out of every three S&P 500 stocks rose, while declines in AI-linked stocks weighed on the cap-weighted indexes.
- The VIX spot price was 18.41 on June 26, down 0.48, or 2.54%, with a prior close of 18.89.

## U.S. Macro Data

- The final June 2026 University of Michigan consumer sentiment index was 49.5, up from 44.8 in May and down from 60.7 in June 2025. Current economic conditions were 47.7. Consumer expectations were 50.7.
- June 2026 year-ahead inflation expectations were 4.6%, down from 4.8% in May. Long-run inflation expectations were 3.3%, down from 3.9% in May.
- May 2026 personal income increased $181.6 billion, or 0.7% month over month. Disposable personal income increased $164.9 billion, or 0.7%. Personal consumption expenditures increased $156.1 billion, or 0.7%.
- May 2026 real disposable personal income increased 0.3%. The personal saving rate was 3.0%.
- May 2026 PCE prices were up 4.1% from a year earlier. PCE prices excluding food and energy were up 3.4% from a year earlier.
- Q1 2026 real GDP increased at a 2.1% annual rate in the third estimate, compared with a 0.5% increase in Q4 2025. The third estimate revised real GDP up 0.5 percentage point from the prior estimate.
- Initial unemployment claims were 215,000 for the week ending June 20, 2026, down 12,000 from the revised prior-week level of 227,000. The four-week moving average was 224,250, up 750 from the prior revised average.
- May 2026 manufactured durable-goods new orders decreased $15.6 billion, or 4.5%, to $332.1 billion after an 8.5% April increase. Excluding transportation, new orders increased 1.3%; excluding defense, new orders decreased 4.6%.

## Rates And Policy Calendar

- The Federal Reserve's June 26 H.15 release showed latest available observations for June 25, 2026: effective federal funds rate 3.63%, bank prime loan rate 6.75%, 3-month Treasury constant maturity 3.84%, 2-year 4.09%, 5-year 4.15%, 10-year 4.40%, 20-year 4.87%, and 30-year 4.86%.
- On June 26, the 10-year Treasury yield was reported at 4.37%, down from 4.40% late Thursday.
- On June 17, 2026, the FOMC maintained the target range for the federal funds rate at 3.50% to 3.75%.
- June FOMC minutes are scheduled for July 8, 2026 at 2:00 PM ET. The next scheduled FOMC meeting is July 28-29, 2026.

## Energy, Commodities, Crypto, And Geopolitics

- For the week ending June 19, 2026, U.S. commercial crude oil inventories excluding the Strategic Petroleum Reserve decreased by 6.1 million barrels to 412.1 million barrels, about 7% below the five-year average.
- Gasoline inventories increased by 2.1 million barrels and were 5% below the five-year average. Distillate inventories increased by 3.1 million barrels and were 10% below the five-year average.
- U.S. crude refinery inputs averaged 17.1 million barrels per day for the week ending June 19, down 81,000 barrels per day from the prior week. Refineries operated at 96.1% capacity utilization.
- On June 26, Brent crude was reported at $72.60, down 3.8%. WTI crude settled at $69.23.
- On June 26, the U.S. struck Iran in response to a drone attack on a cargo ship in the Strait of Hormuz a day earlier. U.S. Central Command said the military struck missile and drone locations and coastal radar sites.
- Comex gold ended the week at $4,078.70 per troy ounce, down 3.44% for the week. Comex silver ended the week at $59.217 per ounce, down 10.62% for the week.
- Bitcoin was quoted at $58,980.50 at 9:15 AM ET on June 26, down $2,293.69 from the prior morning quote.

## Business Activity

- The June 2026 flash U.S. Composite Output PMI was 52.2, up from 51.5 in May. The flash U.S. Services Business Activity Index was 51.3, up from 50.7. The flash U.S. Manufacturing PMI was 55.7, up from 55.1.
- The June U.S. flash Manufacturing Output Index was 57.7, up from 56.6, and a 59-month high.
- The June flash U.S. PMI release described faster growth, lower employment, elevated price inflation, and supplier delivery times lengthening to the greatest extent since August 2022.

## Company And Sector Facts

- Micron reported fiscal Q3 2026 revenue of $41.46 billion, compared with $23.86 billion in the prior quarter and $9.30 billion in the year-earlier quarter.
- Micron reported fiscal Q3 2026 GAAP net income of $28.24 billion, or $24.67 per diluted share, and non-GAAP net income of $28.86 billion, or $25.11 per diluted share.
- Micron guided fiscal Q4 2026 revenue to $50.0 billion plus or minus $1.0 billion, gross margin around 86%, and non-GAAP diluted EPS of $31.00 plus or minus $1.00.
- Micron said HBM4 built on 1-beta DRAM technology was in high-volume shipments for its lead customer's platform; HBM4E development was underway with volume production expected in calendar 2027.
- On June 26, Micron fell 6.7% and was reported as the heaviest weight on the S&P 500 during that session.
- On June 26, health care stocks were among the strongest upward forces on the market after a European Medicines Agency committee recommended several medicines for approval or indication extensions.
- ON Semiconductor fell 23.7% on June 26 after announcing an all-stock agreement to buy Synaptics in a deal valued at roughly $7 billion.

## Scheduled Dates

- The June 2026 Employment Situation is scheduled for July 2, 2026 at 8:30 AM ET.
- The full May manufacturers' shipments, inventories, and orders report is scheduled for July 2, 2026 at 10:00 AM ET.
- Friday, July 3, 2026 is the observed Independence Day market holiday on the NYSE calendar.
- U.S. international trade in goods and services for May 2026 is scheduled for July 7, 2026 at 8:30 AM ET.
- June FOMC minutes are scheduled for July 8, 2026 at 2:00 PM ET.
- June 2026 CPI and Real Earnings are scheduled for July 14, 2026 at 8:30 AM ET.
- June 2026 PPI is scheduled for July 15, 2026 at 8:30 AM ET.
- June 2026 import and export prices are scheduled for July 17, 2026 at 8:30 AM ET.
- State employment and unemployment for June 2026 is scheduled for July 21, 2026 at 10:00 AM ET.
- The advance June durable-goods report is scheduled for July 27, 2026 at 8:30 AM ET.
- The next FOMC meeting is scheduled for July 28-29, 2026.
- June 2026 personal income and outlays and the Q2 2026 GDP advance estimate are scheduled for July 30, 2026 at 8:30 AM ET.

## Measurement Notes

- GDP and PCE releases are estimates and are subject to scheduled revisions.
- Durable-goods data are advance estimates; the full May report is scheduled for July 2, 2026.
- Weekly claims data are advance readings and prior weeks may be revised.
- Flash PMI readings are preliminary and based on most, but not all, monthly survey responses.
- Federal Reserve H.15 daily Treasury observations in the June 26 release carried latest available table observations through June 25.
- Commodity and crypto prices can differ by contract, venue, and timestamp.

## Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-06-26
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-26 | 0.00% | 0.00% | 0.00% | 0.00% | 2.61% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-26 | 0.07% | 0.31% | 1.75% | 3.87% | 2.92% | 0.24% | -0.01% | 76.19% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-06-26 | -2.38% | -2.61% | 6.16% | 20.46% | 0.00% | 16.69% | -4.49% | 52.38% | -3.78% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-26 | -1.82% | -1.65% | 7.28% | 21.73% | 0.96% | 16.80% | -4.36% | 52.38% | -2.96% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-26 | -4.50% | -3.04% | 13.51% | 29.97% | -0.43% | 31.42% | -7.03% | 47.62% | -5.21% | 1.35 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-26 | -3.37% | -5.22% | -0.69% | 13.98% | -2.61% | 21.39% | -8.21% | 47.62% | -7.47% | 1.23 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-26 | 0.24% | 2.35% | 15.06% | 27.95% | 4.96% | 14.94% | -2.40% | 57.14% | -0.68% | 0.76 | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-26 | 0.58% | 2.76% | 13.75% | 24.84% | 5.37% | 15.81% | -2.40% | 61.90% | -0.31% | 1.02 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-26 | 1.43% | 3.50% | 19.75% | 40.64% | 6.11% | 21.81% | -3.55% | 61.90% | 0.00% | 1.30 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-26 | 2.10% | 3.45% | 20.77% | 42.84% | 6.06% | 17.71% | -2.75% | 57.14% | 0.00% | 1.06 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-26 | 1.52% | -0.63% | 18.01% | 26.06% | 1.98% | 10.85% | -2.93% | 47.62% | -1.48% | 0.32 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-26 | 3.85% | 3.16% | 6.59% | 7.58% | 5.77% | 15.11% | -3.09% | 61.90% | -1.45% | 0.08 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-26 | -3.78% | 4.08% | 27.98% | 38.34% | 6.69% | 44.70% | -7.46% | 61.90% | -5.64% | 1.47 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-26 | -5.28% | -1.68% | 23.90% | 45.03% | 0.93% | 42.53% | -10.89% | 52.38% | -8.52% | 1.65 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-26 | -2.74% | -8.43% | -9.47% | 1.02% | -5.82% | 16.08% | -9.27% | 42.86% | -11.06% | 0.70 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-26 | -2.19% | -5.72% | -5.92% | 7.21% | -3.11% | 22.46% | -7.02% | 47.62% | -7.78% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-26 | 2.40% | 0.85% | 9.65% | 8.59% | 3.46% | 17.28% | -3.58% | 42.86% | -4.70% | -0.01 | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-26 | 7.80% | 8.24% | 3.63% | 21.55% | 10.85% | 20.64% | -3.34% | 57.14% | 0.00% | 0.38 | pass |
| FINANCIALS | XLF | us_sector | 2026-06-26 | 0.35% | 4.55% | -2.85% | 5.04% | 7.16% | 14.14% | -1.44% | 57.14% | -4.20% | 0.68 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-26 | 0.41% | 4.21% | 15.87% | 26.28% | 6.83% | 23.30% | -3.69% | 52.38% | -1.59% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-06-26 | 0.85% | -4.85% | 23.49% | 29.49% | -2.24% | 23.22% | -8.48% | 47.62% | -13.32% | -0.15 | pass |
| MATERIALS | XLB | us_sector | 2026-06-26 | -0.03% | 1.20% | 12.82% | 19.71% | 3.81% | 21.38% | -3.93% | 52.38% | -2.98% | 0.81 | pass |
| UTILITIES | XLU | us_sector | 2026-06-26 | 3.88% | 3.00% | 9.44% | 17.01% | 5.61% | 18.27% | -4.52% | 71.43% | -1.91% | 0.20 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-26 | 4.05% | 2.26% | 13.38% | 14.23% | 4.87% | 19.14% | -3.31% | 57.14% | 0.00% | 0.34 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-26 | 0.71% | 1.09% | 0.14% | 3.23% | 3.70% | 5.21% | -0.86% | 61.90% | -1.77% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-26 | 0.70% | 2.82% | 1.45% | 3.86% | 5.43% | 8.61% | -1.20% | 61.90% | -2.36% | 0.14 | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-26 | 0.28% | 0.09% | 1.35% | 3.61% | 2.70% | 4.31% | -0.98% | 57.14% | -0.38% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-26 | 0.39% | 0.90% | 0.86% | 4.91% | 3.51% | 4.97% | -0.81% | 47.62% | -0.48% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-26 | -0.22% | 0.14% | 1.55% | 5.31% | 2.75% | 3.75% | -0.59% | 47.62% | -0.26% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-26 | 0.44% | 0.88% | 0.95% | 4.29% | 3.49% | 4.04% | -0.57% | 61.90% | -0.73% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-26 | -2.42% | -0.67% | 13.12% | 28.54% | 1.94% | 24.06% | -4.85% | 61.90% | -2.53% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-26 | -3.60% | -2.72% | 8.57% | 21.59% | -0.11% | 24.32% | -5.67% | 42.86% | -4.34% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-06-26 | -1.29% | -1.12% | 5.67% | 17.22% | 1.49% | 17.33% | -2.94% | 47.62% | -1.95% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-06-26 | -3.59% | 1.10% | 15.23% | 30.86% | 3.71% | 27.40% | -5.14% | 66.67% | -4.30% | 1.16 | pass |
| CHINA | MCHI | international_equity | 2026-06-26 | -4.34% | -8.38% | -17.06% | -7.39% | -5.77% | 20.80% | -11.15% | 38.10% | -23.22% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-06-26 | -0.04% | 2.08% | -7.95% | -11.04% | 4.69% | 16.15% | -3.04% | 57.14% | -11.28% | 0.62 | pass |
| GOLD | IAU | commodities | 2026-06-26 | -3.49% | -8.56% | -10.29% | 21.91% | -5.95% | 30.09% | -12.28% | 52.38% | -24.62% | 0.65 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-26 | -3.82% | -9.83% | 17.99% | 25.85% | -7.22% | 18.59% | -12.58% | 33.33% | -16.08% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-26 | -7.31% | 2.71% | 67.17% | 121.33% | 5.32% | 65.96% | -10.69% | 57.14% | -8.57% | 2.23 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-26 | -1.00% | -5.19% | -18.39% | -18.85% | -2.58% | 46.79% | -21.29% | 28.57% | -25.11% | 1.19 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-26 | -5.46% | -3.00% | 22.56% | 45.53% | -0.38% | 50.36% | -12.52% | 57.14% | -9.97% | 1.84 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-26 | -7.19% | -11.63% | 5.55% | 41.15% | -9.02% | 42.68% | -14.06% | 33.33% | -14.06% | 2.13 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-26 | 1.06% | 4.14% | 17.01% | 14.47% | 6.75% | 40.39% | -11.74% | 42.86% | -9.42% | 1.07 | pass |
| SOLAR | TAN | clean_energy | 2026-06-26 | -6.16% | -19.37% | 11.84% | 65.70% | -16.76% | 51.99% | -23.10% | 38.10% | -23.10% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-06-26 | -7.64% | -12.06% | 0.29% | 61.08% | -9.45% | 46.69% | -19.23% | 38.10% | -18.63% | 1.72 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-26 | 0.55% | 1.75% | 9.38% | 18.63% | 4.36% | 12.76% | -2.04% | 61.90% | -0.82% | 0.75 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-26 | 10.53% | 15.68% | 24.45% | 86.53% | 18.29% | 34.93% | -6.53% | 71.43% | 0.00% | 1.06 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-26 | 5.42% | 8.67% | 14.32% | 29.45% | 11.28% | 21.50% | -3.08% | 76.19% | 0.00% | 0.85 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-26 | -0.92% | 2.81% | 8.73% | 28.99% | 5.42% | 29.03% | -4.54% | 47.62% | -5.38% | 1.01 | pass |
| CANADA | EWC | country_equity | 2026-06-26 | -0.12% | -0.32% | 5.97% | 27.59% | 2.29% | 15.07% | -3.20% | 57.14% | -2.33% | 0.80 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-26 | 0.66% | -1.72% | 4.92% | 19.20% | 0.89% | 14.13% | -3.01% | 38.10% | -4.65% | 0.74 | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-26 | -2.07% | -1.96% | 6.31% | 9.15% | 0.65% | 19.56% | -4.78% | 47.62% | -6.27% | 0.94 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-26 | -10.00% | -0.51% | 105.84% | 180.39% | 2.10% | 96.03% | -19.16% | 38.10% | -10.00% | 2.61 | pass |
| TAIWAN | EWT | country_equity | 2026-06-26 | -6.53% | -0.16% | 63.14% | 85.88% | 2.46% | 47.89% | -8.51% | 57.14% | -7.82% | 1.67 | pass |
| BRAZIL | EWZ | country_equity | 2026-06-26 | 2.79% | -3.07% | 10.68% | 28.78% | -0.46% | 21.36% | -6.70% | 38.10% | -16.13% | 1.02 | pass |
| MEXICO | EWW | country_equity | 2026-06-26 | -2.53% | -3.87% | 7.49% | 29.24% | -1.26% | 24.20% | -6.47% | 33.33% | -5.85% | 0.93 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-26 | -5.59% | -6.56% | -8.42% | 28.19% | -3.95% | 37.17% | -9.38% | 52.38% | -21.09% | 1.60 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-26 | 0.48% | 0.94% | 1.30% | 5.48% | 3.55% | 4.55% | -0.80% | 66.67% | -0.67% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-26 | 0.25% | 0.93% | 2.01% | 6.46% | 3.54% | 2.24% | -0.35% | 57.14% | -0.15% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-26 | -0.20% | 1.01% | 2.21% | 10.20% | 3.62% | 5.98% | -1.02% | 47.62% | -0.20% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-26 | 0.33% | 0.84% | 1.33% | 2.46% | 3.45% | 3.23% | -0.66% | 61.90% | -0.50% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-06-26 | -10.47% | -21.07% | -25.08% | 59.81% | -18.46% | 53.32% | -24.25% | 42.86% | -49.55% | 1.67 | pass |
| COPPER | CPER | commodities | 2026-06-26 | -3.94% | -2.99% | 4.24% | 17.76% | -0.38% | 33.84% | -10.57% | 57.14% | -8.05% | 1.24 | pass |
| AGRICULTURE | DBA | commodities | 2026-06-26 | 0.64% | -2.44% | 4.44% | 6.22% | 0.17% | 10.53% | -4.86% | 33.33% | -6.72% | 0.07 | pass |
| OIL | USO | commodities | 2026-06-26 | -8.17% | -19.50% | 54.03% | 43.33% | -16.89% | 43.53% | -25.12% | 33.33% | -31.04% | -1.01 | pass |
| US_DOLLAR | UUP | currencies | 2026-06-26 | 0.57% | 2.56% | 5.52% | 9.13% | 5.17% | 4.83% | -0.43% | 52.38% | -0.25% | -0.13 | pass |
| EURO | FXE | currencies | 2026-06-26 | -0.64% | -2.01% | -2.96% | -2.05% | 0.60% | 5.40% | -2.66% | 52.38% | -5.11% | 0.12 | pass |
| YEN | FXY | currencies | 2026-06-26 | -0.25% | -1.44% | -3.46% | -11.08% | 1.17% | 2.75% | -1.67% | 23.81% | -11.57% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-26 | -4.97% | -20.26% | -31.77% | -44.64% | -17.65% | 46.95% | -21.04% | 28.57% | -52.52% | 1.82 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-26 | -7.69% | -23.22% | -46.30% | -35.59% | -20.61% | 69.50% | -24.18% | 28.57% | -67.50% | 2.99 | pass |

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
