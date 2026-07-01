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

- Round ID: CB-2026-06-30-1M
- Decision date: 2026-06-30
- Research cutoff UTC: 2026-07-01T06:30:00Z
- Decision deadline UTC: 2026-07-01T07:30:00Z
- Horizon: one month
- Entry date: 2026-06-30
- Exit date: 2026-07-30
- Scoring window: 2026-06-30 to 2026-07-30; optimize for this one month window only.
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

Research cutoff UTC: 2026-07-01T06:30:00Z.

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. A mechanical full-universe price, risk, and benchmark-relative appendix follows this briefing in the model input.

## U.S. Market Snapshot Through The June 30 Close

- On June 30, 2026, the Dow Jones Industrial Average closed at 52,319.20, up 136.46 points or 0.26%; the S&P 500 closed at 7,499.36, up 0.79%; and the Nasdaq Composite closed at 26,213.72, up 1.52%.
- Public market reports for the June 30 close showed the Dow up 8.9% for the first half of 2026, the S&P 500 up 9.6%, the Nasdaq Composite up more than 12%, and the Russell 2000 up nearly 22%.
- Public market reports said the Russell 2000's first-half gain was its strongest first-half performance since 1991.
- Semiconductor-related reports for June 30 said Nvidia rose 2.6%, AMD rose 7.7%, Intel rose 6%, and the VanEck Semiconductor ETF rose more than 3% that day. The same reports said SMH was up 82% year to date, SMH was up around 70% for the second quarter, SOXX was up about 94% for the second quarter, Micron was up about 240% for the quarter, and Nvidia was up less than 14% for the quarter.

## Rates, Inflation, Growth, And Policy

- Market data reports after the June 30 economic releases showed the 2-year Treasury yield at 4.131% and the 10-year Treasury yield at 4.4%.
- The Federal Reserve's June 17, 2026 FOMC statement maintained the target range for the federal funds rate at 3.5% to 3.75%.
- The Bureau of Economic Analysis reported that May personal income rose 0.7%, disposable personal income rose 0.7%, current-dollar personal consumption expenditures rose 0.7%, and real personal consumption expenditures rose 0.3%.
- The May PCE price index rose 0.4% month over month and 4.1% year over year. Core PCE rose 0.3% month over month and 3.4% year over year.
- The BEA's third estimate for Q1 2026 showed real GDP growth at a 2.1% annual rate. Real final sales to private domestic purchasers were reported at 1.7%, and corporate profits from current production rose $74.4 billion.

## Labor, Consumer, And Demand Data

- The Bureau of Labor Statistics reported May job openings unchanged at 7.6 million and the job-openings rate unchanged at 4.6%.
- May hires were unchanged at 5.2 million, total separations changed little at 5.1 million, and quits were little changed at 3.1 million.
- The Conference Board reported that the Consumer Confidence Index increased by 0.6 points to 91.2 in June from a downwardly revised 90.6 in May.
- The Conference Board reported the Present Situation Index at 116.4, down 3.0 points, and the Expectations Index at 74.4, up 3.0 points.
- The Conference Board said its June preliminary survey period was June 1-23 and included an extension of the U.S.-Iran ceasefire agreement. The same release said the share of consumers saying jobs were hard to get rose to 22.5%.

## Commodities, Currency, And Global Context

- Reuters reported on June 30 that Brent crude was $73.18 per barrel at 10:51 a.m. EDT and WTI crude was $70.45 per barrel.
- Reuters also reported that both Brent and WTI were on track for their largest monthly and quarterly declines since early 2020, while investors monitored U.S.-Iran diplomatic efforts and the ceasefire status.
- Public market reports said Treasury yields and the U.S. dollar moved higher after June 30 economic indicators.
- Public market reports said the Japanese yen weakened near a 40-year low against the U.S. dollar around the June 30 close.

## Scheduled Items Before The One-Week Exit Close

- Wednesday, July 1, 2026: June ISM Manufacturing PMI is scheduled for 10:00 a.m. ET.
- Thursday, July 2, 2026: the June U.S. employment report is scheduled before the U.S. equity open, and U.S. bond markets have a holiday-related early close.
- Friday, July 3, 2026: NYSE-listed U.S. equity markets are closed for the observed Independence Day holiday.
- Monday, July 6, 2026: final S&P U.S. Services PMI and June ISM Services PMI are scheduled.
- Tuesday, July 7, 2026: the May U.S. trade balance is scheduled before the U.S. equity open.

## Scheduled Items Before The One-Month Exit Close

- Wednesday, July 8, 2026: June FOMC meeting minutes, wholesale inventories, and consumer credit are scheduled.
- Thursday, July 9, 2026: initial jobless claims and existing home sales are scheduled.
- Friday, July 10, 2026: TSMC June monthly sales are scheduled.
- Tuesday, July 14, 2026: JPMorgan Chase and Wells Fargo list Q2 2026 earnings events.
- Thursday, July 16, 2026: TSMC lists Q2 2026 results.
- Wednesday, July 29, 2026: the next scheduled FOMC policy decision is listed.
- Thursday, July 30, 2026: first preliminary Q2 GDP, personal income, and PCE data are scheduled.

## Data Status

- Facts above are fixed at the research cutoff. Scheduled items are calendar entries, not released outcomes at the cutoff.
- Price history in the following mechanical appendix is descriptive context, not a forecast.
- This briefing does not rank, recommend, analyze, or map facts to CapitalBench options. The option list and appendix order are not signals of expected return.

## Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-06-30
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-30 | 0.00% | 0.00% | 0.00% | 0.00% | 1.03% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-30 | 0.07% | 0.27% | 1.75% | 3.83% | 1.30% | 0.24% | -0.01% | 70.00% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-06-30 | 1.80% | -1.03% | 9.28% | 22.20% | 0.00% | 18.29% | -4.49% | 50.00% | -1.43% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-30 | 2.04% | -0.38% | 10.19% | 23.18% | 0.65% | 18.02% | -4.36% | 50.00% | -0.87% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-30 | 3.19% | -0.15% | 19.16% | 34.13% | 0.88% | 33.88% | -7.03% | 45.00% | -1.20% | 1.36 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-30 | 3.64% | -2.79% | 4.32% | 17.41% | -1.76% | 24.22% | -8.21% | 45.00% | -3.49% | 1.23 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-30 | 0.61% | 2.20% | 15.18% | 26.86% | 3.23% | 15.31% | -2.40% | 55.00% | -0.81% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-30 | 2.40% | 3.62% | 16.16% | 25.96% | 4.65% | 16.37% | -2.40% | 65.00% | 0.00% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-30 | 1.74% | 3.69% | 21.63% | 40.68% | 4.73% | 22.13% | -3.55% | 65.00% | 0.00% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-30 | 1.68% | 3.80% | 21.88% | 42.58% | 4.83% | 17.73% | -2.60% | 55.00% | -0.10% | 1.04 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-30 | -0.18% | -1.65% | 16.65% | 24.03% | -0.62% | 10.85% | -2.93% | 45.00% | -2.64% | 0.31 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-30 | 0.93% | 3.92% | 5.26% | 5.14% | 4.95% | 14.03% | -1.89% | 65.00% | -2.57% | 0.07 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-30 | 3.96% | 8.67% | 35.88% | 43.66% | 9.70% | 47.39% | -7.46% | 60.00% | -0.69% | 1.48 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-30 | 3.44% | -0.14% | 31.34% | 51.25% | 0.89% | 43.67% | -10.89% | 50.00% | -3.77% | 1.65 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-30 | -0.13% | -7.15% | -8.91% | -0.05% | -6.12% | 17.72% | -8.43% | 45.00% | -10.26% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-30 | 3.09% | -2.77% | -2.17% | 8.76% | -1.74% | 23.41% | -4.21% | 55.00% | -5.44% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-30 | -0.78% | 0.89% | 7.64% | 5.45% | 1.92% | 16.95% | -3.57% | 45.00% | -6.54% | -0.03 | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-30 | 4.26% | 6.61% | 2.78% | 19.76% | 7.64% | 20.50% | -3.34% | 60.00% | -1.29% | 0.37 | pass |
| FINANCIALS | XLF | us_sector | 2026-06-30 | -0.50% | 4.30% | -2.01% | 3.95% | 5.33% | 14.28% | -1.44% | 60.00% | -4.13% | 0.67 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-30 | 3.97% | 7.25% | 19.04% | 27.17% | 8.28% | 23.95% | -3.69% | 65.00% | 0.00% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-06-30 | -2.48% | -4.98% | 19.74% | 29.12% | -3.95% | 22.46% | -8.96% | 45.00% | -14.50% | -0.15 | pass |
| MATERIALS | XLB | us_sector | 2026-06-30 | -0.08% | -0.25% | 12.06% | 17.87% | 0.78% | 22.83% | -3.93% | 55.00% | -4.43% | 0.78 | pass |
| UTILITIES | XLU | us_sector | 2026-06-30 | 0.60% | 2.72% | 6.95% | 14.12% | 3.75% | 15.13% | -1.87% | 75.00% | -3.74% | 0.18 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-30 | -1.37% | 0.96% | 9.79% | 9.94% | 1.99% | 19.80% | -3.31% | 60.00% | -2.67% | 0.32 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-30 | 0.48% | 0.25% | -0.38% | 2.60% | 1.28% | 5.61% | -0.76% | 60.00% | -2.24% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-30 | 0.26% | 1.17% | 0.22% | 2.40% | 2.20% | 9.85% | -1.20% | 55.00% | -3.41% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-30 | 0.49% | -0.46% | 1.03% | 3.22% | 0.57% | 4.61% | -0.98% | 50.00% | -0.63% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-30 | 0.15% | 0.11% | 0.45% | 4.10% | 1.14% | 5.48% | -0.80% | 45.00% | -0.87% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-30 | 0.13% | 0.09% | 1.59% | 5.15% | 1.12% | 3.88% | -0.59% | 45.00% | -0.09% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-30 | 0.27% | 0.25% | 0.50% | 3.79% | 1.29% | 4.37% | -0.55% | 60.00% | -1.09% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-30 | 1.54% | -0.21% | 14.27% | 28.58% | 0.83% | 24.77% | -4.85% | 60.00% | -1.57% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-30 | 0.56% | -0.20% | 11.06% | 23.81% | 0.83% | 25.16% | -5.67% | 50.00% | -2.53% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-06-30 | 1.58% | 0.82% | 7.42% | 17.76% | 1.86% | 18.14% | -2.55% | 60.00% | -0.35% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-06-30 | 0.56% | 0.87% | 15.79% | 29.81% | 1.90% | 28.09% | -5.14% | 70.00% | -3.82% | 1.14 | pass |
| CHINA | MCHI | international_equity | 2026-06-30 | -1.52% | -6.79% | -15.22% | -5.64% | -5.75% | 21.43% | -11.15% | 40.00% | -22.39% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-06-30 | 0.65% | 1.71% | -7.92% | -11.30% | 2.74% | 16.17% | -1.71% | 60.00% | -11.55% | 0.60 | pass |
| GOLD | IAU | commodities | 2026-06-30 | -2.35% | -11.67% | -7.59% | 21.09% | -10.64% | 29.88% | -11.17% | 45.00% | -25.66% | 0.63 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-30 | -1.85% | -9.88% | 18.33% | 26.45% | -8.84% | 17.42% | -12.58% | 30.00% | -16.02% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-30 | 5.44% | 9.51% | 80.53% | 135.91% | 10.54% | 69.52% | -10.69% | 60.00% | -1.95% | 2.24 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-30 | 3.76% | -10.86% | -15.30% | -17.25% | -9.83% | 33.10% | -21.29% | 25.00% | -23.07% | 1.19 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-30 | 3.57% | -2.54% | 27.75% | 50.30% | -1.51% | 50.49% | -12.52% | 55.00% | -6.46% | 1.83 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-30 | 4.64% | -7.45% | 14.48% | 48.67% | -6.42% | 46.20% | -12.87% | 40.00% | -8.07% | 2.14 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-30 | 6.79% | 1.00% | 24.70% | 19.53% | 2.03% | 29.92% | -11.74% | 40.00% | -4.66% | 1.09 | pass |
| SOLAR | TAN | clean_energy | 2026-06-30 | 1.01% | -19.99% | 19.42% | 72.65% | -18.96% | 51.77% | -21.34% | 40.00% | -19.99% | 1.75 | pass |
| METALS_MINING | XME | commodities | 2026-06-30 | -3.58% | -14.54% | 2.23% | 59.65% | -13.51% | 45.42% | -19.75% | 35.00% | -19.44% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-30 | 1.86% | 2.28% | 11.02% | 19.01% | 3.31% | 13.78% | -2.04% | 55.00% | -0.13% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-30 | 7.63% | 15.88% | 30.19% | 91.67% | 16.91% | 34.41% | -4.39% | 70.00% | -0.04% | 1.06 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-30 | 2.37% | 8.15% | 15.70% | 29.08% | 9.18% | 20.62% | -3.08% | 80.00% | -0.43% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-30 | 2.75% | 3.04% | 12.21% | 29.16% | 4.07% | 27.78% | -3.00% | 55.00% | -3.13% | 1.00 | pass |
| CANADA | EWC | country_equity | 2026-06-30 | -0.05% | -1.53% | 6.65% | 26.47% | -0.50% | 15.37% | -3.20% | 55.00% | -2.61% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-30 | 1.25% | -0.27% | 5.85% | 20.12% | 0.77% | 14.64% | -2.39% | 45.00% | -3.85% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-30 | 0.50% | -2.36% | 8.14% | 10.37% | -1.33% | 19.78% | -4.78% | 50.00% | -5.62% | 0.94 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-30 | 5.05% | -1.91% | 104.73% | 187.68% | -0.88% | 95.80% | -19.16% | 40.00% | -7.89% | 2.58 | pass |
| TAIWAN | EWT | country_equity | 2026-06-30 | 3.20% | 5.67% | 70.48% | 97.93% | 6.70% | 49.40% | -8.51% | 60.00% | -2.62% | 1.68 | pass |
| BRAZIL | EWZ | country_equity | 2026-06-30 | 1.02% | -3.01% | 8.88% | 25.06% | -1.98% | 21.78% | -5.84% | 40.00% | -16.54% | 0.99 | pass |
| MEXICO | EWW | country_equity | 2026-06-30 | 0.72% | -2.62% | 9.90% | 28.56% | -1.59% | 25.12% | -5.91% | 40.00% | -5.98% | 0.91 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-30 | -1.16% | -7.03% | -6.79% | 26.65% | -6.00% | 36.86% | -8.61% | 55.00% | -20.92% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-30 | 0.19% | 0.07% | 0.77% | 5.04% | 1.10% | 4.82% | -0.67% | 65.00% | -1.09% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-30 | 0.34% | 0.68% | 1.83% | 6.35% | 1.71% | 2.31% | -0.35% | 50.00% | -0.13% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-30 | 0.19% | 0.43% | 2.17% | 9.56% | 1.47% | 6.31% | -1.02% | 45.00% | -0.39% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-30 | 0.10% | 0.44% | 1.25% | 2.23% | 1.48% | 3.25% | -0.62% | 60.00% | -0.67% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-06-30 | -4.06% | -21.75% | -22.48% | 62.97% | -20.72% | 54.70% | -23.84% | 45.00% | -49.37% | 1.64 | pass |
| COPPER | CPER | commodities | 2026-06-30 | 1.10% | -2.91% | 7.04% | 19.25% | -1.88% | 32.80% | -10.57% | 55.00% | -7.07% | 1.22 | pass |
| AGRICULTURE | DBA | commodities | 2026-06-30 | 0.26% | -2.13% | 4.30% | 5.67% | -1.10% | 10.80% | -3.67% | 35.00% | -7.17% | 0.06 | pass |
| OIL | USO | commodities | 2026-06-30 | -4.33% | -17.55% | 52.62% | 45.59% | -16.51% | 39.89% | -25.12% | 35.00% | -30.41% | -0.98 | pass |
| US_DOLLAR | UUP | currencies | 2026-06-30 | -0.14% | 2.71% | 5.03% | 9.30% | 3.74% | 4.92% | -0.56% | 55.00% | -0.42% | -0.13 | pass |
| EURO | FXE | currencies | 2026-06-30 | 0.39% | -2.04% | -2.38% | -2.37% | -1.01% | 5.55% | -2.39% | 50.00% | -4.80% | 0.12 | pass |
| YEN | FXY | currencies | 2026-06-30 | -0.63% | -2.05% | -3.85% | -11.73% | -1.02% | 2.84% | -1.86% | 20.00% | -11.99% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-30 | -5.72% | -20.03% | -33.19% | -45.61% | -19.00% | 48.28% | -17.78% | 30.00% | -53.30% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-30 | -5.03% | -21.78% | -46.75% | -37.65% | -20.74% | 72.89% | -22.30% | 30.00% | -67.50% | 2.95 | pass |

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
