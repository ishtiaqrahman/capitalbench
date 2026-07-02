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

- Round ID: CB-2026-07-01-1M
- Decision date: 2026-07-01
- Research cutoff UTC: 2026-07-02T01:25:00Z
- Decision deadline UTC: 2026-07-02T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-01
- Exit date: 2026-07-31
- Scoring window: 2026-07-01 to 2026-07-31; optimize for this one month window only.
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

# Market Briefing

Research cutoff UTC: 2026-07-02T01:25:00Z.

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. A mechanical full-universe price, risk, and benchmark-relative appendix follows this briefing in the model input.

## U.S. Market Snapshot Through The July 1 Close

- On July 1, 2026, the S&P 500 closed at 7,483.23, down 16.13 points or 0.2%; the Dow Jones Industrial Average closed at 52,305.24, down 13.96 points or less than 0.1%; the Nasdaq Composite closed at 26,040.03, down 173.69 points or 0.7%; and the Russell 2000 closed at 3,012.59, down 11.78 points or 0.4%.
- Public market reports for the July 1 close showed week-to-date gains of 1.8% for the S&P 500, 0.8% for the Dow, 2.9% for the Nasdaq, and 0.1% for the Russell 2000.
- Public market reports for the July 1 close showed year-to-date gains of 9.3% for the S&P 500, 8.8% for the Dow, 12.0% for the Nasdaq, and 21.4% for the Russell 2000.
- Public market reports said most U.S. stocks rose on July 1, while declines in some influential technology companies kept the major indexes lower. The same reports noted declines among some recent AI-related stocks, including Micron Technology.

## Rates, Inflation, Growth, And Policy

- Market data after the July 1 close showed gold continuous futures at $4,048.80, down 0.82%; WTI front-month crude at $67.99, down 0.86%; the U.S. Dollar Index at 101.41, up 0.01%; bitcoin at $59,968, up 0.02%; ether at $1,603.70, down 0.76%; and the U.S. 10-year Treasury note at 4.479%.
- The Federal Reserve's June 17, 2026 FOMC statement maintained the target range for the federal funds rate at 3.50% to 3.75%.
- The Bureau of Economic Analysis reported that May personal income rose 0.7%, disposable personal income rose 0.7%, current-dollar personal consumption expenditures rose 0.7%, and real personal consumption expenditures rose 0.3%.
- The May PCE price index rose 0.4% month over month and 4.1% year over year. Core PCE rose 0.3% month over month and 3.4% year over year.
- The BEA's third estimate for Q1 2026 showed real GDP growth at a 2.1% annual rate, following 0.5% in Q4 2025. Real final sales to private domestic purchasers rose 1.7%, and corporate profits from current production rose $74.4 billion.

## Labor, Manufacturing, Consumer, And Demand Data

- ADP reported that U.S. private-sector employment increased by 98,000 jobs in June 2026 and annual pay was up 4.4% year over year.
- ADP reported June job-stayer pay gains of 4.4% and job-changer pay gains of 6.6%. Its sector detail showed goods-producing employment up 2,000 and service-providing employment up 96,000.
- ISM reported the June Manufacturing PMI at 53.3, down 0.7 percentage point from May. New orders were 56.0, production was 52.2, and employment was 49.7.
- The Bureau of Labor Statistics reported May job openings unchanged at 7.6 million and the job-openings rate unchanged at 4.6%.
- May hires were unchanged at 5.2 million, total separations changed little at 5.1 million, quits changed little at 3.1 million, and layoffs/discharges were unchanged at 1.7 million.
- The Conference Board reported that the Consumer Confidence Index increased by 0.6 points to 91.2 in June from a revised 90.6 in May.
- The Conference Board reported the Present Situation Index at 116.4, down 3.0 points, and the Expectations Index at 74.4, up 3.0 points.
- The Conference Board said the share of consumers saying jobs were hard to get rose to 22.5%, and the labor-market differential fell 2.6 percentage points to +2.4.

## Scheduled Items Before The One-Week Exit Close

- Thursday, July 2, 2026: the June U.S. Employment Situation is scheduled for 8:30 a.m. ET. Public economic-calendar median forecasts list 115,000 payroll jobs, a 4.3% unemployment rate, 0.3% monthly hourly wage growth, and 3.5% year-over-year hourly wage growth.
- Thursday, July 2, 2026: initial jobless claims for the week of June 27 and May factory orders are scheduled.
- Friday, July 3, 2026: NYSE-listed U.S. equity markets are closed for the observed Independence Day holiday.
- Monday, July 6, 2026: final S&P U.S. Services PMI and June ISM Services PMI are scheduled.
- Tuesday, July 7, 2026: the May U.S. trade balance is scheduled.
- Wednesday, July 8, 2026: wholesale inventories, the June FOMC meeting minutes, and consumer credit are scheduled.

## Scheduled Items Before The One-Month Exit Close

- Thursday, July 9, 2026: initial jobless claims and existing home sales are scheduled.
- Friday, July 10, 2026: TSMC June 2026 monthly sales are scheduled.
- Tuesday, July 14, 2026: JPMorgan Chase and Wells Fargo list Q2 2026 earnings events.
- Thursday, July 16, 2026: TSMC lists Q2 2026 results.
- Wednesday, July 29, 2026: the next scheduled FOMC policy decision is listed.
- Thursday, July 30, 2026: first preliminary Q2 GDP and the next personal income and PCE release are scheduled.

## Data Status

- Facts above are fixed at the research cutoff. Scheduled items and economic-calendar forecasts are not released outcomes at the cutoff.
- Price history in the following mechanical appendix is descriptive context, not a forecast.
- This briefing does not rank, recommend, analyze, or map facts to CapitalBench options. The option list and appendix order are not signals of expected return.

## Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close
- As-of date requested: 2026-07-01
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-01 | 0.00% | 0.00% | 0.00% | 0.00% | 1.43% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-01 | 0.08% | 0.29% | 1.77% | 3.84% | 1.73% | 0.24% | -0.01% | 71.43% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-01 | 1.71% | -1.43% | 9.94% | 22.08% | 0.00% | 17.83% | -4.49% | 47.62% | -1.57% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-01 | 1.84% | -0.82% | 10.81% | 22.92% | 0.61% | 17.57% | -4.36% | 47.62% | -1.08% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-01 | 2.05% | -2.26% | 18.32% | 33.21% | -0.82% | 33.43% | -7.03% | 42.86% | -2.71% | 1.36 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-01 | 2.80% | -4.38% | 4.15% | 17.56% | -2.95% | 23.75% | -8.21% | 42.86% | -4.38% | 1.23 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-01 | 1.20% | 3.02% | 16.75% | 26.44% | 4.46% | 15.01% | -2.40% | 57.14% | -0.22% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-01 | 0.90% | 2.80% | 16.37% | 23.33% | 4.24% | 16.37% | -2.40% | 61.90% | -0.87% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-01 | 0.89% | 3.82% | 22.10% | 38.72% | 5.26% | 21.66% | -3.55% | 61.90% | -0.38% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-01 | 1.43% | 4.59% | 23.13% | 39.99% | 6.03% | 17.28% | -2.60% | 57.14% | 0.00% | 1.04 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-01 | 0.41% | -0.24% | 18.02% | 22.05% | 1.20% | 10.70% | -2.93% | 47.62% | -2.21% | 0.31 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-01 | 0.74% | 5.71% | 6.52% | 4.87% | 7.14% | 13.69% | -1.89% | 66.67% | -2.13% | 0.07 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-01 | -0.09% | 3.64% | 31.34% | 39.53% | 5.07% | 49.02% | -7.46% | 57.14% | -4.96% | 1.48 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-01 | 1.40% | -5.07% | 29.24% | 48.69% | -3.63% | 43.42% | -10.89% | 47.62% | -6.24% | 1.66 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-01 | 3.00% | -4.83% | -6.24% | 3.12% | -3.39% | 19.81% | -8.43% | 47.62% | -8.08% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-01 | 2.62% | 0.12% | -0.71% | 9.05% | 1.55% | 22.95% | -4.21% | 57.14% | -4.79% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-01 | -1.35% | 2.26% | 8.59% | 4.44% | 3.69% | 16.53% | -3.57% | 47.62% | -6.29% | -0.03 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-01 | 4.04% | 8.39% | 3.94% | 18.73% | 9.82% | 19.99% | -3.34% | 61.90% | -0.75% | 0.37 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-01 | 1.97% | 6.88% | 0.88% | 5.63% | 8.32% | 15.47% | -1.44% | 61.90% | -2.04% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-01 | 1.75% | 6.62% | 18.82% | 25.47% | 8.05% | 23.83% | -3.69% | 61.90% | -1.01% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-01 | -1.42% | -7.18% | 19.73% | 27.41% | -5.75% | 21.91% | -9.47% | 42.86% | -14.98% | -0.15 | pass |
| MATERIALS | XLB | us_sector | 2026-07-01 | -0.27% | 0.57% | 13.42% | 15.33% | 2.01% | 22.29% | -3.93% | 57.14% | -4.07% | 0.78 | pass |
| UTILITIES | XLU | us_sector | 2026-07-01 | -1.69% | 4.54% | 6.27% | 12.30% | 5.97% | 15.69% | -3.10% | 71.43% | -4.95% | 0.18 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-01 | -0.74% | 2.99% | 11.18% | 9.57% | 4.42% | 19.31% | -3.31% | 61.90% | -2.34% | 0.32 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-01 | -0.41% | 0.18% | -0.29% | 2.54% | 1.62% | 5.54% | -0.76% | 57.14% | -2.47% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-01 | -1.76% | 0.43% | 0.35% | 1.46% | 1.86% | 9.93% | -1.84% | 52.38% | -4.06% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-01 | -0.08% | -0.68% | 1.04% | 3.09% | 0.75% | 4.52% | -0.98% | 47.62% | -0.81% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-01 | -0.52% | -0.08% | 0.66% | 3.76% | 1.35% | 5.39% | -0.80% | 42.86% | -1.08% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-01 | 0.14% | 0.15% | 1.67% | 5.26% | 1.58% | 3.78% | -0.59% | 42.86% | -0.10% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-01 | -0.36% | 0.15% | 0.59% | 3.73% | 1.59% | 4.29% | -0.55% | 57.14% | -1.24% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-01 | 0.11% | -1.59% | 13.42% | 27.06% | -0.16% | 24.52% | -4.85% | 57.14% | -2.80% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-01 | 0.42% | -1.87% | 10.28% | 22.34% | -0.44% | 24.66% | -5.67% | 47.62% | -3.30% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-07-01 | 0.94% | 0.50% | 6.91% | 16.65% | 1.93% | 17.98% | -2.55% | 57.14% | -1.21% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-07-01 | 0.48% | 0.66% | 15.86% | 30.46% | 2.10% | 27.40% | -5.14% | 66.67% | -4.04% | 1.14 | pass |
| CHINA | MCHI | international_equity | 2026-07-01 | 0.18% | -6.38% | -13.66% | -5.01% | -4.95% | 21.41% | -11.15% | 42.86% | -21.63% | 0.90 | pass |
| INDIA | INDA | international_equity | 2026-07-01 | -0.85% | 2.54% | -8.95% | -11.87% | 3.98% | 15.86% | -1.71% | 57.14% | -11.87% | 0.60 | pass |
| GOLD | IAU | commodities | 2026-07-01 | 1.29% | -9.86% | -6.42% | 20.72% | -8.43% | 29.38% | -11.17% | 47.62% | -25.21% | 0.63 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-01 | 0.00% | -11.70% | 19.09% | 24.98% | -10.26% | 16.98% | -12.58% | 28.57% | -16.55% | -0.15 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-01 | 0.25% | 2.08% | 72.29% | 125.63% | 3.52% | 70.75% | -10.69% | 57.14% | -7.24% | 2.24 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-01 | 8.32% | -13.32% | -11.67% | -13.75% | -11.88% | 34.92% | -21.29% | 28.57% | -20.74% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-01 | 0.38% | -8.37% | 25.11% | 47.42% | -6.93% | 50.15% | -12.52% | 52.38% | -9.28% | 1.83 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-01 | 5.01% | -6.76% | 13.76% | 51.72% | -5.32% | 45.19% | -12.87% | 38.10% | -9.30% | 2.14 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-01 | 8.82% | -3.15% | 27.85% | 23.09% | -1.71% | 29.69% | -11.74% | 42.86% | -3.32% | 1.09 | pass |
| SOLAR | TAN | clean_energy | 2026-07-01 | -0.62% | -18.74% | 17.67% | 64.02% | -17.31% | 50.69% | -21.34% | 38.10% | -21.82% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-07-01 | -2.67% | -18.07% | 0.86% | 55.95% | -16.63% | 44.61% | -21.38% | 33.33% | -21.38% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-01 | 1.44% | 2.40% | 12.31% | 17.98% | 3.84% | 13.44% | -2.04% | 57.14% | 0.00% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-01 | 4.57% | 17.27% | 28.51% | 89.27% | 18.71% | 34.21% | -4.39% | 66.67% | -1.11% | 1.06 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-01 | 2.99% | 12.17% | 18.90% | 27.03% | 13.60% | 20.58% | -3.08% | 80.95% | 0.00% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-01 | 3.25% | 6.14% | 13.74% | 32.48% | 7.57% | 27.10% | -3.00% | 57.14% | -2.55% | 1.00 | pass |
| CANADA | EWC | country_equity | 2026-07-01 | 0.66% | -1.31% | 7.43% | 26.56% | 0.12% | 14.98% | -3.20% | 57.14% | -2.56% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-01 | 1.08% | -0.19% | 5.96% | 19.21% | 1.25% | 14.35% | -2.39% | 42.86% | -4.27% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-01 | -0.75% | -3.56% | 7.26% | 8.44% | -2.13% | 20.00% | -4.78% | 47.62% | -7.16% | 0.94 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-01 | -5.96% | -14.40% | 90.80% | 164.83% | -12.96% | 97.35% | -19.16% | 38.10% | -15.37% | 2.59 | pass |
| TAIWAN | EWT | country_equity | 2026-07-01 | 0.93% | -0.69% | 66.36% | 92.01% | 0.75% | 49.14% | -8.51% | 57.14% | -5.24% | 1.69 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-01 | 0.97% | -3.26% | 8.61% | 24.16% | -1.83% | 21.42% | -5.84% | 38.10% | -17.31% | 0.99 | pass |
| MEXICO | EWW | country_equity | 2026-07-01 | 2.01% | -1.92% | 10.16% | 27.38% | -0.49% | 24.48% | -5.91% | 38.10% | -5.98% | 0.91 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-01 | 0.88% | -5.27% | -6.89% | 24.66% | -3.83% | 35.98% | -8.61% | 52.38% | -21.50% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-01 | -0.41% | 0.04% | 0.84% | 4.95% | 1.47% | 4.74% | -0.67% | 61.90% | -1.26% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-01 | 0.16% | 0.64% | 1.82% | 6.26% | 2.08% | 2.25% | -0.35% | 52.38% | -0.13% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-01 | -0.16% | 0.43% | 2.35% | 9.33% | 1.86% | 6.15% | -1.02% | 42.86% | -0.41% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-01 | -0.24% | 0.56% | 1.27% | 2.04% | 2.00% | 3.21% | -0.62% | 57.14% | -0.77% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-01 | 3.48% | -20.82% | -16.83% | 63.70% | -19.39% | 53.51% | -23.84% | 47.62% | -49.26% | 1.64 | pass |
| COPPER | CPER | commodities | 2026-07-01 | 2.48% | -6.88% | 6.44% | 17.87% | -5.45% | 32.20% | -10.57% | 52.38% | -8.35% | 1.22 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-01 | 1.13% | -1.40% | 5.25% | 8.47% | 0.04% | 10.90% | -3.67% | 38.10% | -6.51% | 0.06 | pass |
| OIL | USO | commodities | 2026-07-01 | -2.84% | -23.79% | 49.32% | 39.69% | -22.35% | 39.38% | -26.69% | 33.33% | -32.49% | -0.97 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-01 | -0.14% | 2.63% | 5.40% | 9.66% | 4.06% | 4.83% | -0.56% | 57.14% | -0.14% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-01 | 0.24% | -2.15% | -2.81% | -2.83% | -0.72% | 5.52% | -2.39% | 47.62% | -5.18% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-01 | -0.48% | -1.88% | -3.82% | -11.88% | -0.44% | 2.79% | -1.88% | 19.05% | -12.01% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-01 | 0.38% | -16.03% | -31.52% | -43.18% | -14.59% | 48.24% | -17.78% | 33.33% | -52.31% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-01 | 2.27% | -19.32% | -45.65% | -32.99% | -17.89% | 72.14% | -22.30% | 33.33% | -66.68% | 2.94 | pass |

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
