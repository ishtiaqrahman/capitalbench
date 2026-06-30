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

- Round ID: CB-2026-06-29-1W
- Decision date: 2026-06-29
- Research cutoff UTC: 2026-06-29T23:55:00Z
- Decision deadline UTC: 2026-06-30T03:30:00Z
- Horizon: one week
- Entry date: 2026-06-29
- Exit date: 2026-07-06
- Scoring window: 2026-06-29 to 2026-07-06; optimize for this one week window only.
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

Research cutoff: 2026-06-29T23:55:00Z.

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. A mechanical full-universe price, risk, and benchmark-relative appendix follows this briefing in the model input.

## U.S. Market Close

- On June 29, 2026, the S&P 500 closed at 7,440.43, up 86.41 points, or 1.2%. The Dow Jones Industrial Average closed at 52,182.74, up 306.63 points, or 0.6%. The Nasdaq Composite closed at 25,820.14, up 522.53 points, or 2.1%. The Russell 2000 closed at 3,010.42, up 0.33 points, or less than 0.1%.
- The S&P 500 and Nasdaq Composite ended five-day losing streaks on June 29. The Dow Jones Industrial Average closed above 52,000 for the first time.
- Through the June 29 close, year-to-date index moves were: S&P 500 up 8.7%, Dow up 8.6%, Nasdaq up 11.1%, Russell 2000 up 21.3%.
- On June 29, AI-linked stocks rebounded after sharp swings the prior week. Communication services and consumer discretionary were reported among the stronger S&P 500 sectors during the session, while small caps were near flat.
- Cboe displayed VIX spot in the high teens on June 29. The public page showed a point-in-time VIX spot value of 17.65 during the observed session.

## U.S. Macro Data

- May 2026 personal income increased $181.6 billion, or 0.7% month over month. Disposable personal income increased $164.9 billion, or 0.7%. Personal consumption expenditures increased $156.1 billion, or 0.7%.
- May 2026 real disposable personal income increased 0.3%. The personal saving rate was 3.0%.
- May 2026 PCE prices were up 4.1% from a year earlier. PCE prices excluding food and energy were up 3.4% from a year earlier.
- Q1 2026 real GDP increased at a 2.1% annual rate in the third estimate, compared with a 0.5% increase in Q4 2025. The third estimate revised real GDP up 0.5 percentage point from the prior estimate.
- Initial unemployment claims were 215,000 for the week ending June 20, 2026, down 12,000 from the revised prior-week level of 227,000. The four-week moving average was 224,250.
- May 2026 manufactured durable-goods new orders decreased $15.6 billion, or 4.5%, to $332.1 billion after an 8.5% April increase. Excluding transportation, new orders increased 1.3%; excluding defense, new orders decreased 4.6%.

## Rates And Policy Calendar

- On June 17, 2026, the FOMC maintained the target range for the federal funds rate at 3.50% to 3.75% by a 12-0 vote and reaffirmed ample-reserves policy.
- The June 17 FOMC statement said economic activity was expanding at a solid pace despite elevated uncertainty, job gains had kept pace with the workforce, and inflation remained elevated relative to the 2% goal.
- The Federal Reserve's June 29 H.15 page identified June 29, 2026 as the current release date.
- The prior June 26 H.15 release showed latest table observations for June 25, 2026: effective federal funds rate 3.63%, bank prime loan rate 6.75%, 3-month Treasury constant maturity 3.84%, 2-year 4.09%, 5-year 4.15%, 10-year 4.40%, 20-year 4.87%, and 30-year 4.86%.
- On June 29, the 10-year Treasury yield was reported as little changed from Friday's close above 4.37%, while Treasury yields inched higher during the session.
- The next scheduled FOMC meeting is July 28-29, 2026.

## Energy, Commodities, Crypto, And Geopolitics

- On June 29, U.S. and Iranian officials were reported to be moving toward renewed talks after weekend military exchanges and a halt in attacks.
- On June 29, WTI crude settled up 2.2% at $70.75 per barrel. Front-month Brent rose 1.6% to $73.15 ahead of expiry.
- On June 29, gold was reported lower during the equity session and traded around $4,050 per troy ounce in afternoon market coverage.
- For the week ending June 19, 2026, U.S. commercial crude oil inventories excluding the Strategic Petroleum Reserve decreased by 6.1 million barrels to 412.1 million barrels, about 7% below the five-year average.
- Gasoline inventories increased by 2.1 million barrels and were 5% below the five-year average. Distillate inventories increased by 3.1 million barrels and were 10% below the five-year average.
- U.S. crude refinery inputs averaged 17.1 million barrels per day for the week ending June 19, down 81,000 barrels per day from the prior week. Refineries operated at 96.1% capacity utilization.
- Bitcoin was quoted around $60,400 before the June 29 equity open and was reported near the $60,000 area during the session.

## Business Activity

- The June 2026 flash U.S. Composite Output PMI was 52.2, up from 51.5 in May. The flash U.S. Services Business Activity Index was 51.3, up from 50.7. The flash U.S. Manufacturing PMI was 55.7, up from 55.1.
- The June U.S. flash Manufacturing Output Index was 57.7, up from 56.6, and a 59-month high.
- The June flash U.S. PMI release described faster output growth, softer employment, elevated price inflation, and supplier delivery times lengthening to the greatest extent since August 2022.

## Company And Sector Facts

- Micron reported fiscal Q3 2026 revenue of $41.46 billion, compared with $23.86 billion in the prior quarter and $9.30 billion in the year-earlier quarter.
- Micron reported fiscal Q3 2026 GAAP net income of $28.24 billion, or $24.67 per diluted share, and non-GAAP net income of $28.86 billion, or $25.11 per diluted share.
- Micron guided fiscal Q4 2026 revenue to $50.0 billion plus or minus $1.0 billion, gross margin around 86%, and non-GAAP diluted EPS of $31.00 plus or minus $1.00.
- Micron said HBM4 built on 1-beta DRAM technology was in high-volume shipments for its lead customer's platform; HBM4E development was underway with volume production expected in calendar 2027.
- Micron's post-earnings commentary was reported as describing memory demand running ahead of supply, with no clear supply catch-up line before 2027.
- First-half 2026 chipmaker gains reported on June 29 included Sandisk up 780%, Western Digital up 240%, Micron up 296%, and Seagate up 226%.
- Comcast announced a plan to split into two publicly traded companies through a spinoff of NBCUniversal and Sky, separating broadband from media and entertainment.
- Comcast was reported as planning to keep as much as a 19.9% stake in NBCUniversal for up to a year following the spinoff.
- Alphabet replaced Verizon in the Dow Jones Industrial Average effective before the open on June 29, 2026.

## Scheduled Dates

- May 2026 JOLTS is scheduled for June 30, 2026 at 10:00 AM ET.
- June 2026 consumer confidence is scheduled for June 30, 2026 at 10:00 AM ET.
- June 2026 ADP employment and ISM Manufacturing PMI are scheduled for July 1, 2026.
- The June 2026 Employment Situation is scheduled for July 2, 2026 at 8:30 AM ET.
- Friday, July 3, 2026 is the observed Independence Day market holiday on NYSE and Nasdaq calendars.
- Final June 2026 services and composite PMI data are scheduled for July 6, 2026.
- June 2026 CPI and Real Earnings are scheduled for July 14, 2026 at 8:30 AM ET.
- June 2026 PPI is scheduled for July 15, 2026 at 8:30 AM ET.
- June 2026 import and export prices are scheduled for July 17, 2026 at 8:30 AM ET.
- State employment and unemployment for June 2026 is scheduled for July 21, 2026 at 10:00 AM ET.
- The next FOMC meeting is scheduled for July 28-29, 2026.
- The Q2 2026 GDP advance estimate and June 2026 personal income and outlays are scheduled for July 30, 2026 at 8:30 AM ET.

## Measurement Notes

- GDP and PCE releases are estimates and are subject to scheduled revisions.
- Durable-goods data are advance estimates; the full May report is scheduled for July 2, 2026.
- Weekly claims data are advance readings and prior weeks may be revised.
- Flash PMI readings are preliminary and based on most, but not all, monthly survey responses.
- Federal Reserve H.15 daily Treasury observations can update after the round's research cutoff.
- Commodity, volatility, and crypto prices can differ by contract, venue, and timestamp.

## Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-06-29
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-29 | 0.00% | 0.00% | 0.00% | 0.00% | 1.79% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-29 | 0.08% | 0.27% | 1.76% | 3.84% | 2.07% | 0.24% | -0.01% | 73.68% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-06-29 | -0.46% | -1.79% | 8.30% | 21.84% | 0.00% | 18.52% | -4.49% | 47.37% | -2.19% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-29 | -0.17% | -1.17% | 9.14% | 22.82% | 0.62% | 18.24% | -4.36% | 47.37% | -1.65% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-29 | -1.88% | -1.82% | 16.90% | 32.75% | -0.03% | 34.18% | -7.03% | 42.11% | -2.85% | 1.36 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-29 | 0.18% | -4.51% | 2.27% | 16.13% | -2.71% | 23.72% | -8.21% | 42.11% | -5.19% | 1.23 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-29 | -0.32% | 2.33% | 15.28% | 27.59% | 4.13% | 15.70% | -2.40% | 57.89% | -0.68% | 0.75 | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-29 | 0.60% | 2.84% | 14.90% | 25.01% | 4.64% | 16.67% | -2.40% | 63.16% | 0.00% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-29 | 0.26% | 3.19% | 20.14% | 40.19% | 4.98% | 22.71% | -3.55% | 63.16% | -0.29% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-29 | 1.51% | 3.84% | 21.24% | 42.69% | 5.63% | 18.19% | -2.60% | 57.89% | -0.07% | 1.05 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-29 | 0.92% | -0.97% | 17.51% | 25.44% | 0.82% | 10.86% | -2.93% | 47.37% | -1.97% | 0.31 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-29 | 3.21% | 4.88% | 6.25% | 6.98% | 6.67% | 13.69% | -1.89% | 68.42% | -1.67% | 0.07 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-29 | -2.67% | 6.51% | 32.81% | 42.35% | 8.30% | 48.31% | -7.46% | 57.89% | -2.67% | 1.47 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-29 | -3.51% | -2.82% | 27.42% | 48.65% | -1.03% | 43.51% | -10.89% | 47.37% | -6.35% | 1.65 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-29 | 0.95% | -6.51% | -7.96% | 1.45% | -4.71% | 18.17% | -8.44% | 47.37% | -9.64% | 0.70 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-29 | 1.90% | -2.91% | -2.70% | 7.99% | -1.12% | 24.05% | -4.21% | 52.63% | -5.57% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-29 | 2.66% | 2.47% | 9.14% | 7.65% | 4.26% | 16.23% | -3.58% | 47.37% | -5.08% | -0.02 | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-29 | 7.12% | 8.01% | 4.05% | 22.11% | 9.81% | 20.06% | -3.34% | 63.16% | 0.00% | 0.38 | pass |
| FINANCIALS | XLF | us_sector | 2026-06-29 | 0.04% | 4.51% | -2.05% | 5.03% | 6.31% | 14.57% | -1.44% | 63.16% | -3.93% | 0.67 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-29 | 0.53% | 5.82% | 17.12% | 26.11% | 7.62% | 24.32% | -3.69% | 63.16% | -0.74% | 0.96 | pass |
| ENERGY | XLE | us_sector | 2026-06-29 | -0.89% | -4.13% | 21.74% | 29.54% | -2.33% | 22.99% | -8.48% | 47.37% | -13.74% | -0.15 | pass |
| MATERIALS | XLB | us_sector | 2026-06-29 | -1.86% | -0.59% | 11.66% | 17.38% | 1.21% | 23.43% | -3.93% | 52.63% | -4.75% | 0.78 | pass |
| UTILITIES | XLU | us_sector | 2026-06-29 | 2.91% | 4.26% | 8.81% | 16.32% | 6.06% | 13.99% | -1.87% | 78.95% | -2.29% | 0.19 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-29 | 2.04% | 3.01% | 12.28% | 13.01% | 4.80% | 18.65% | -3.31% | 63.16% | -0.71% | 0.33 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-29 | 1.13% | 0.77% | 0.03% | 3.54% | 2.56% | 5.38% | -0.76% | 63.16% | -1.73% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-29 | 1.58% | 2.37% | 1.17% | 4.63% | 4.17% | 8.95% | -1.20% | 57.89% | -2.26% | 0.14 | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-29 | 0.88% | -0.03% | 1.44% | 3.93% | 1.76% | 4.47% | -0.98% | 52.63% | -0.20% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-29 | 0.85% | 0.69% | 0.91% | 5.27% | 2.49% | 5.17% | -0.80% | 47.37% | -0.30% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-29 | 0.09% | 0.14% | 1.74% | 5.60% | 1.93% | 3.98% | -0.59% | 47.37% | -0.04% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-29 | 0.75% | 0.65% | 0.86% | 4.62% | 2.44% | 4.20% | -0.55% | 63.16% | -0.70% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-29 | -2.03% | -0.66% | 13.86% | 28.40% | 1.13% | 25.38% | -4.85% | 57.89% | -2.03% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-29 | -3.36% | -1.05% | 10.52% | 22.96% | 0.74% | 25.62% | -5.67% | 47.37% | -3.36% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-06-29 | -0.20% | 0.29% | 7.19% | 17.40% | 2.09% | 18.55% | -2.55% | 57.89% | -0.89% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-06-29 | -3.88% | 0.81% | 15.57% | 29.15% | 2.61% | 28.87% | -5.14% | 68.42% | -3.88% | 1.15 | pass |
| CHINA | MCHI | international_equity | 2026-06-29 | -3.92% | -7.21% | -15.31% | -6.21% | -5.42% | 21.79% | -11.15% | 36.84% | -22.75% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-06-29 | -1.48% | 1.28% | -8.02% | -11.96% | 3.07% | 16.58% | -1.71% | 57.89% | -11.93% | 0.60 | pass |
| GOLD | IAU | commodities | 2026-06-29 | -4.15% | -11.65% | -7.45% | 22.51% | -9.86% | 30.63% | -11.17% | 47.37% | -25.64% | 0.63 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-29 | -3.18% | -10.10% | 18.74% | 26.29% | -8.31% | 17.61% | -12.58% | 26.32% | -16.23% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-29 | -5.52% | 5.52% | 73.52% | 127.69% | 7.31% | 70.28% | -10.69% | 57.89% | -5.52% | 2.23 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-29 | 2.95% | -11.56% | -16.28% | -16.58% | -9.77% | 33.42% | -21.29% | 21.05% | -23.67% | 1.19 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-29 | -4.28% | -4.60% | 24.83% | 48.20% | -2.81% | 51.05% | -12.52% | 52.63% | -8.44% | 1.82 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-29 | -1.27% | -10.14% | 10.59% | 45.71% | -8.34% | 45.82% | -12.87% | 36.84% | -10.73% | 2.13 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-29 | 5.98% | -0.52% | 22.30% | 19.29% | 1.27% | 30.01% | -11.74% | 36.84% | -6.09% | 1.09 | pass |
| SOLAR | TAN | clean_energy | 2026-06-29 | -5.74% | -22.09% | 14.90% | 68.72% | -20.29% | 51.40% | -21.34% | 36.84% | -22.09% | 1.75 | pass |
| METALS_MINING | XME | commodities | 2026-06-29 | -7.55% | -14.87% | 1.09% | 61.06% | -13.07% | 46.43% | -19.75% | 31.58% | -19.75% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-29 | 1.64% | 2.42% | 10.99% | 19.73% | 4.21% | 14.12% | -2.04% | 57.89% | 0.00% | 0.75 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-29 | 8.54% | 15.93% | 28.43% | 91.58% | 17.72% | 35.18% | -4.39% | 73.68% | 0.00% | 1.06 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-29 | 3.83% | 8.01% | 14.69% | 28.79% | 9.81% | 21.14% | -3.08% | 78.95% | -0.56% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-29 | 1.54% | 1.64% | 10.35% | 28.15% | 3.43% | 28.24% | -3.00% | 52.63% | -4.44% | 1.00 | pass |
| CANADA | EWC | country_equity | 2026-06-29 | -0.69% | -1.78% | 6.31% | 27.85% | 0.01% | 15.74% | -3.20% | 52.63% | -2.86% | 0.79 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-29 | 1.01% | -0.25% | 6.34% | 20.13% | 1.54% | 15.04% | -2.39% | 47.37% | -3.84% | 0.74 | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-29 | -1.20% | -2.55% | 7.65% | 11.12% | -0.75% | 20.30% | -4.78% | 47.37% | -5.80% | 0.94 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-29 | -9.83% | -4.05% | 100.06% | 185.46% | -2.25% | 97.99% | -19.16% | 36.84% | -9.90% | 2.58 | pass |
| TAIWAN | EWT | country_equity | 2026-06-29 | -5.15% | 2.93% | 67.05% | 91.27% | 4.72% | 49.82% | -8.51% | 57.89% | -5.15% | 1.68 | pass |
| BRAZIL | EWZ | country_equity | 2026-06-29 | 0.82% | -2.87% | 11.38% | 28.29% | -1.08% | 22.38% | -5.84% | 42.11% | -16.42% | 0.99 | pass |
| MEXICO | EWW | country_equity | 2026-06-29 | 0.21% | -1.52% | 9.54% | 30.51% | 0.28% | 25.50% | -5.91% | 42.11% | -4.91% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-29 | -2.64% | -6.63% | -5.29% | 29.86% | -4.83% | 37.97% | -8.61% | 57.89% | -20.58% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-29 | 0.76% | 0.54% | 1.25% | 5.94% | 2.34% | 4.60% | -0.67% | 68.42% | -0.62% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-29 | 0.36% | 0.77% | 1.97% | 6.60% | 2.56% | 2.33% | -0.35% | 52.63% | -0.05% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-29 | 0.44% | 0.83% | 2.45% | 10.62% | 2.62% | 6.28% | -1.02% | 47.37% | 0.00% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-29 | 0.52% | 0.63% | 1.46% | 2.53% | 2.42% | 3.24% | -0.62% | 63.16% | -0.48% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-06-29 | -10.58% | -22.90% | -20.19% | 61.50% | -21.11% | 55.30% | -23.84% | 42.11% | -50.11% | 1.64 | pass |
| COPPER | CPER | commodities | 2026-06-29 | -4.07% | -4.19% | 8.92% | 17.56% | -2.40% | 33.13% | -10.57% | 52.63% | -8.30% | 1.22 | pass |
| AGRICULTURE | DBA | commodities | 2026-06-29 | -0.53% | -2.72% | 3.35% | 4.31% | -0.92% | 10.76% | -3.67% | 31.58% | -7.73% | 0.06 | pass |
| OIL | USO | commodities | 2026-06-29 | -4.98% | -17.05% | 53.83% | 46.12% | -15.26% | 40.93% | -25.12% | 36.84% | -29.99% | -0.98 | pass |
| US_DOLLAR | UUP | currencies | 2026-06-29 | 0.04% | 2.57% | 5.15% | 8.58% | 4.36% | 5.05% | -0.56% | 52.63% | -0.56% | -0.13 | pass |
| EURO | FXE | currencies | 2026-06-29 | 0.02% | -2.03% | -2.59% | -1.74% | -0.24% | 5.70% | -2.39% | 52.63% | -4.79% | 0.12 | pass |
| YEN | FXY | currencies | 2026-06-29 | -0.23% | -1.67% | -3.13% | -10.90% | 0.13% | 2.69% | -1.48% | 21.05% | -11.65% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-29 | -6.36% | -17.90% | -30.78% | -43.71% | -16.10% | 49.19% | -17.21% | 31.58% | -52.05% | 1.81 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-29 | -6.28% | -19.47% | -44.62% | -33.00% | -17.68% | 74.58% | -22.30% | 31.58% | -66.55% | 2.97 | pass |

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
