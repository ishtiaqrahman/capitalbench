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

- Round ID: CB-2026-06-24-1M
- Decision date: 2026-06-24
- Research cutoff UTC: 2026-06-24T21:20:00Z
- Decision deadline UTC: 2026-06-25T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-24
- Exit date: 2026-07-24
- Scoring window: 2026-06-24 to 2026-07-24; optimize for this one month window only.
- Close-to-close scoring: the entry price is the adjusted close on the entry date, and the exit price is the adjusted close on the exit date after regular trading ends.
- Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.
- Input-bias control: treat fact inclusion, section order, grouping, and price-context table order as context, not recommendations; do not infer expected return from mention count or placement.
- Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history as one input, not as a standalone reason to select or allocate to an option.
- Continuation evidence: when a holding or selection relies on recent price strength, compare it with the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, drawdown, and reversal risk before the exit close. Do not invent support that is not in the input.
- Entry rule: Use adjusted close prices on Wednesday, June 24, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, July 24, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
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

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. A mechanical full-universe price, risk, and benchmark-relative appendix follows this briefing in the model input.

## 2. Research And Evaluation Setup

| field | value |
| --- | --- |
| research cutoff | 2026-06-24T21:20:00Z |
| decision deadline | 2026-06-25T02:30:00Z |
| weekly round | CB-2026-06-24-1W |
| weekly entry and exit dates | 2026-06-24 to 2026-07-01 |
| monthly round | CB-2026-06-24-1M |
| monthly entry and exit dates | 2026-06-24 to 2026-07-24 |
| entry snapshot | adjusted close prices for Wednesday, June 24, 2026 |
| model access rule | no tool use and no web access |
| shared-input rule | competing models receive the same frozen factual briefing, fixed ETF option universe, and mechanical price/risk appendix |
| mechanical entry-price status | generated from the frozen full-universe June 24 adjusted-close table |

## 3. Latest Macro Datapoints

| indicator | latest value | period | date | publisher | status |
| --- | --- | --- | --- | --- | --- |
| FOMC target range | 3.50%-3.75% | June 17 decision | 2026-06-17 | Federal Reserve | observed |
| CPI headline | +0.5% MoM, +4.2% YoY | May 2026 | 2026-06-10 | BLS | observed |
| CPI core | +0.2% MoM, +2.9% YoY | May 2026 | 2026-06-10 | BLS | observed |
| CPI energy | +3.9% MoM, +23.5% YoY | May 2026 | 2026-06-10 | BLS | observed |
| CPI gasoline | +7.0% MoM, +40.5% YoY | May 2026 | 2026-06-10 | BLS | observed |
| CPI shelter | +0.3% MoM, +3.4% YoY | May 2026 | 2026-06-10 | BLS | observed |
| Retail and food services sales | $763.7 billion, +0.9% MoM, +6.9% YoY | May 2026 | 2026-06-17 | U.S. Census | observed |
| Retail trade sales | +1.0% MoM, +7.5% YoY | May 2026 | 2026-06-17 | U.S. Census | observed |
| Q1 real GDP | +1.6% annualized | second estimate | 2026-05-29 | BEA | observed |
| Q1 real final sales to private domestic purchasers | +2.4% annualized | second estimate | 2026-05-29 | BEA | observed |
| Q1 PCE price index / core PCE price index | +4.5% / +4.4% annualized | second estimate | 2026-05-29 | BEA | observed |
| May PCE price index forecast | headline +0.5% MoM and +4.1% YoY; core +0.3% MoM and +3.4% YoY | May 2026 | 2026-06-18 | Kiplinger citing Wells Fargo economists | forecast |

## 4. Rates, Market, And Cross-Asset Datapoints

| indicator | latest value | period / observation | publisher | status |
| --- | --- | --- | --- | --- |
| Effective federal funds rate | 3.63% | 2026-06-23 | Federal Reserve H.15 | observed |
| 3-month Treasury bill | 3.70% | 2026-06-23 | Federal Reserve H.15 | observed |
| 2-year Treasury | 4.16% | 2026-06-23 | Federal Reserve H.15 | observed |
| 5-year Treasury | 4.27% | 2026-06-23 | Federal Reserve H.15 | observed |
| 10-year Treasury | 4.50% | 2026-06-23 | Federal Reserve H.15 | observed |
| 30-year Treasury | 4.94% | 2026-06-23 | Federal Reserve H.15 | observed |
| 5-year TIPS real yield | 2.03% | 2026-06-23 | Federal Reserve H.15 | observed |
| 10-year TIPS real yield | 2.29% | 2026-06-23 | Federal Reserve H.15 | observed |
| 10-year Treasury market level | 4.40%, down from 4.50% late Tuesday | 2026-06-24 close | AP market report | observed |
| 2-year Treasury market level | 4.15%, down from 4.16% late Tuesday | 2026-06-24 close | AP market report | observed |
| Brent crude | $73.87 per barrel, -3.8% | 2026-06-24 close | AP market report | observed |
| U.S. crude | $70.34 per barrel, -3.9% | 2026-06-24 close | AP market report | observed |
| Gold | $4,008.80 per ounce, -3.4% | 2026-06-24 close | AP market report | observed |

## 5. U.S. Equity Market Close

| index | close | daily change | week-to-date | year-to-date | date | publisher | status |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| S&P 500 | 7,358.22 | -7.24 / -0.1% | -1.9% | +7.5% | 2026-06-24 | AP market close | observed |
| Dow Jones Industrial Average | 51,848.90 | +182.06 / +0.4% | +0.6% | +7.9% | 2026-06-24 | AP market close | observed |
| Nasdaq Composite | 25,476.64 | -110.40 / -0.4% | -3.9% | +9.6% | 2026-06-24 | AP market close | observed |
| Russell 2000 | 2,986.63 | +11.15 / +0.4% | +0.2% | +20.3% | 2026-06-24 | AP market close | observed |

| datapoint | value | date | publisher | status |
| --- | --- | --- | --- | --- |
| S&P 500 breadth note | more stocks rose than fell within the index while several large technology weights pulled the capitalization-weighted index lower | 2026-06-24 | AP market report | observed |
| Microsoft | -2.3% | 2026-06-24 | AP market report | observed |
| Oracle | -4.6% | 2026-06-24 | AP market report | observed |
| Exxon Mobil | -2.0% | 2026-06-24 | AP market report | observed |
| Chevron | -2.6% | 2026-06-24 | AP market report | observed |
| KB Home | +16.7% | 2026-06-24 | AP market report | observed |
| D.R. Horton | +6.7% | 2026-06-24 | AP market report | observed |
| Alphabet Dow inclusion | Alphabet scheduled to replace Verizon in the Dow on Monday, June 29, 2026 | 2026-06-24 | AP market report | scheduled |

## 6. Housing, External Balance, Survey, Energy, And Company Datapoints

| datapoint | value | period | date | publisher | status |
| --- | --- | --- | --- | --- | --- |
| New single-family home sales | 580,000 seasonally adjusted annual rate; -7.3% from April and -6.8% from May 2025 | May 2026 | 2026-06-24 | U.S. Census / HUD | observed |
| New houses for sale | 496,000; 10.3 months of supply | May 2026 | 2026-06-24 | U.S. Census / HUD | observed |
| Median new-home sales price | $424,900; +2.0% from April and virtually unchanged from May 2025 | May 2026 | 2026-06-24 | U.S. Census / HUD | observed |
| U.S. current-account deficit | -$226.8 billion; widened $5.8 billion or 2.6%; 2.9% of current-dollar GDP | Q1 2026 | 2026-06-24 | BEA | observed |
| U.S. net international investment position | -$21.27 trillion; assets $43.37 trillion and liabilities $64.64 trillion | end Q1 2026 | 2026-06-24 | BEA | observed |
| S&P Global U.S. Composite PMI | 52.2 | June flash, data collected 2026-06-11 to 2026-06-22 | 2026-06-23 | S&P Global | observed |
| S&P Global U.S. Services PMI | 51.3 | June flash | 2026-06-23 | S&P Global | observed |
| S&P Global U.S. Manufacturing PMI | 55.7 | June flash | 2026-06-23 | S&P Global | observed |
| S&P Global U.S. Manufacturing Output Index | 57.7 | June flash | 2026-06-23 | S&P Global | observed |
| Commercial crude oil inventories | -6.1 million barrels to 412.1 million barrels; about 7% below five-year average | week ending 2026-06-19 | 2026-06-24 | EIA | observed |
| Gasoline inventories | +2.1 million barrels; 5% below five-year average | week ending 2026-06-19 | 2026-06-24 | EIA | observed |
| Distillate inventories | +3.1 million barrels; about 10% below five-year average | week ending 2026-06-19 | 2026-06-24 | EIA | observed |
| Refinery utilization | 96.1% | week ending 2026-06-19 | 2026-06-24 | EIA | observed |
| Micron fiscal Q3 revenue | $41.46 billion, versus $23.86 billion prior quarter and $9.30 billion year earlier | fiscal Q3 2026, ended 2026-05-28 | 2026-06-24 | Micron | observed |
| Micron fiscal Q3 GAAP / non-GAAP gross margin | 84.6% / 84.9% | fiscal Q3 2026 | 2026-06-24 | Micron | observed |
| Micron fiscal Q4 guidance | revenue $50.0 billion plus or minus $1.0 billion; gross margin about 86%; non-GAAP diluted EPS $31.00 plus or minus $1.00 | fiscal Q4 2026 | 2026-06-24 | Micron | guidance |
| Micron product facts | HBM4 high-volume shipments for lead customer's platform; HBM4E volume production expected in calendar 2027 | fiscal Q3 2026 release | 2026-06-24 | Micron | observed / guidance |

## 7. Scheduled Events

| date | event | entity | status |
| --- | --- | --- | --- |
| 2026-06-25 | GDP third estimate, industries, corporate profits, state GDP, and state personal income, Q1 2026 | BEA | scheduled |
| 2026-06-25 | Personal Income and Outlays, May 2026 | BEA | scheduled |
| 2026-06-25 | Weekly jobless claims, durable goods, and related U.S. economic releases listed in public calendars | U.S. agencies / public economic calendars | scheduled |
| 2026-07-01 | Weekly round exit close | CapitalBench | scheduled |
| 2026-07-03 | Independence Day observed market holiday | Nasdaq / NYSE | scheduled |
| 2026-07-07 | U.S. International Trade in Goods and Services, May 2026 | BEA | scheduled |
| 2026-07-24 | Monthly round exit close | CapitalBench | scheduled |
| 2026-07-30 | GDP advance estimate for Q2 2026 and Personal Income and Outlays, June 2026 | BEA | scheduled |

## 8. Final Neutrality Statement

This briefing provides fixed factual datapoints only. It does not rank, recommend, analyze, or map facts to CapitalBench options. Inclusion, order, grouping, and row count are not evidence of expected return. The mechanical appendix that follows is complete full-universe descriptive context, not a forecast.

## Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-06-24
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-24 | 0.00% | 0.00% | 0.00% | 0.00% | 1.41% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-24 | 0.07% | 0.29% | 1.74% | 3.85% | 1.70% | 0.23% | -0.01% | 75.00% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-06-24 | -0.79% | -1.41% | 6.77% | 22.18% | 0.00% | 16.96% | -4.49% | 50.00% | -3.22% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-24 | -0.58% | -0.86% | 7.33% | 22.77% | 0.55% | 17.22% | -4.36% | 50.00% | -2.86% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-24 | -1.54% | -0.86% | 14.16% | 32.28% | 0.55% | 31.73% | -7.03% | 45.00% | -4.66% | 1.35 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-24 | -1.59% | -4.18% | -0.20% | 16.05% | -2.77% | 21.28% | -7.05% | 50.00% | -6.99% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-24 | 0.26% | 2.30% | 14.18% | 27.20% | 3.71% | 14.32% | -2.40% | 55.00% | -1.14% | 0.76 | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-24 | 1.04% | 3.33% | 13.08% | 24.74% | 4.74% | 15.98% | -2.40% | 60.00% | -0.53% | 1.02 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-24 | 2.35% | 4.31% | 17.89% | 39.77% | 5.72% | 22.28% | -3.55% | 55.00% | -0.50% | 1.30 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-24 | 2.29% | 3.82% | 18.82% | 41.78% | 5.23% | 17.98% | -2.75% | 55.00% | 0.00% | 1.07 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-24 | 0.13% | -2.61% | 16.57% | 24.19% | -1.20% | 10.64% | -2.93% | 40.00% | -2.61% | 0.33 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-24 | 2.08% | 1.00% | 5.04% | 4.95% | 2.41% | 15.14% | -3.48% | 55.00% | -2.84% | 0.09 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-24 | 0.04% | 8.29% | 28.81% | 39.62% | 9.70% | 41.74% | -7.46% | 60.00% | -4.87% | 1.45 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-24 | -1.36% | 1.60% | 25.42% | 48.85% | 3.01% | 43.02% | -10.89% | 50.00% | -7.54% | 1.64 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-24 | -2.18% | -7.49% | -9.26% | 2.52% | -6.08% | 16.43% | -8.45% | 45.00% | -10.76% | 0.71 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-24 | -0.17% | -3.26% | -5.76% | 7.58% | -1.85% | 23.34% | -7.02% | 50.00% | -7.22% | 1.19 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-24 | 1.61% | 0.27% | 9.45% | 6.70% | 1.68% | 17.72% | -3.58% | 45.00% | -5.01% | -0.01 | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-24 | 2.20% | 2.76% | -0.73% | 16.63% | 4.17% | 18.17% | -3.34% | 55.00% | -3.46% | 0.40 | pass |
| FINANCIALS | XLF | us_sector | 2026-06-24 | -0.26% | 3.79% | -2.77% | 5.77% | 5.20% | 14.76% | -1.89% | 55.00% | -3.93% | 0.68 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-24 | 0.59% | 5.17% | 15.02% | 25.83% | 6.58% | 21.87% | -3.69% | 50.00% | -0.87% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-06-24 | -1.31% | -9.30% | 22.40% | 30.11% | -7.89% | 23.78% | -8.48% | 45.00% | -13.75% | -0.14 | pass |
| MATERIALS | XLB | us_sector | 2026-06-24 | -1.29% | 2.11% | 12.52% | 18.85% | 3.52% | 21.39% | -3.93% | 55.00% | -3.81% | 0.81 | pass |
| UTILITIES | XLU | us_sector | 2026-06-24 | 3.08% | 1.06% | 7.80% | 14.74% | 2.47% | 18.57% | -4.92% | 65.00% | -3.31% | 0.21 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-24 | 2.12% | 0.76% | 11.78% | 8.96% | 2.17% | 19.00% | -3.31% | 50.00% | -1.01% | 0.35 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-24 | 0.76% | 1.24% | -0.08% | 3.32% | 2.65% | 5.29% | -0.86% | 60.00% | -2.08% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-24 | 1.22% | 3.59% | 1.14% | 4.54% | 5.00% | 8.80% | -1.20% | 65.00% | -2.34% | 0.14 | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-24 | 0.27% | 0.19% | 0.99% | 3.61% | 1.60% | 4.33% | -0.98% | 55.00% | -0.73% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-24 | 0.59% | 1.34% | 0.77% | 5.08% | 2.75% | 5.11% | -0.81% | 50.00% | -0.56% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-24 | 0.15% | 0.44% | 1.53% | 5.62% | 1.85% | 3.84% | -0.59% | 45.00% | -0.24% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-24 | 0.59% | 1.10% | 0.82% | 4.41% | 2.51% | 4.14% | -0.57% | 60.00% | -0.88% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-24 | -1.88% | 0.27% | 12.91% | 28.78% | 1.68% | 24.11% | -4.85% | 60.00% | -2.91% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-24 | -1.29% | 0.10% | 9.99% | 23.52% | 1.51% | 24.93% | -5.67% | 50.00% | -3.71% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-06-24 | -1.23% | -0.37% | 5.75% | 17.26% | 1.04% | 17.14% | -3.12% | 45.00% | -2.15% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-06-24 | -1.95% | 1.64% | 14.95% | 32.80% | 3.05% | 27.97% | -5.14% | 65.00% | -4.50% | 1.17 | pass |
| CHINA | MCHI | international_equity | 2026-06-24 | -2.96% | -6.79% | -14.58% | -5.70% | -5.38% | 21.27% | -9.48% | 40.00% | -21.77% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-06-24 | 1.16% | 2.56% | -8.11% | -9.43% | 3.97% | 16.46% | -3.04% | 55.00% | -11.15% | 0.63 | pass |
| GOLD | IAU | commodities | 2026-06-24 | -5.84% | -11.58% | -11.09% | 19.64% | -10.17% | 29.96% | -12.28% | 45.00% | -26.17% | 0.66 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-24 | -4.59% | -13.30% | 17.59% | 25.33% | -11.89% | 16.67% | -12.58% | 30.00% | -16.55% | -0.17 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-24 | -0.81% | 7.39% | 69.95% | 128.64% | 8.80% | 65.38% | -10.69% | 55.00% | -7.47% | 2.21 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-24 | -3.35% | -8.32% | -20.37% | -20.23% | -6.91% | 45.13% | -19.98% | 25.00% | -26.83% | 1.21 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-24 | -1.46% | 0.92% | 23.31% | 47.37% | 2.33% | 51.14% | -12.52% | 55.00% | -9.62% | 1.83 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-24 | -5.49% | -8.83% | 4.23% | 45.44% | -7.42% | 43.83% | -13.63% | 40.00% | -13.63% | 2.14 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-24 | -0.51% | -0.57% | 15.23% | 14.09% | 0.84% | 42.27% | -11.74% | 40.00% | -11.15% | 1.08 | pass |
| SOLAR | TAN | clean_energy | 2026-06-24 | -0.50% | -11.81% | 14.35% | 74.08% | -10.40% | 54.43% | -21.33% | 45.00% | -21.33% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-06-24 | -9.37% | -8.35% | -0.47% | 63.20% | -6.94% | 47.43% | -19.23% | 40.00% | -19.23% | 1.73 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-24 | 1.05% | 2.23% | 9.45% | 18.70% | 3.64% | 12.63% | -2.04% | 60.00% | -0.79% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-24 | 7.51% | 13.82% | 18.65% | 79.43% | 15.23% | 35.15% | -6.53% | 70.00% | 0.00% | 1.07 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-24 | 4.57% | 7.25% | 12.15% | 29.69% | 8.66% | 22.45% | -3.44% | 70.00% | 0.00% | 0.86 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-24 | -2.72% | 4.87% | 7.41% | 30.61% | 6.28% | 29.73% | -4.54% | 50.00% | -5.62% | 1.02 | pass |
| CANADA | EWC | country_equity | 2026-06-24 | -1.55% | -1.62% | 5.42% | 27.30% | -0.22% | 15.44% | -3.20% | 50.00% | -3.20% | 0.81 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-24 | -1.02% | -2.10% | 4.58% | 19.24% | -0.69% | 14.00% | -3.40% | 35.00% | -5.30% | 0.74 | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-24 | -2.58% | -1.66% | 6.40% | 10.50% | -0.25% | 20.04% | -4.78% | 40.00% | -6.47% | 0.95 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-24 | -3.81% | 8.37% | 108.52% | 177.62% | 9.78% | 96.63% | -19.16% | 35.00% | -10.01% | 2.59 | pass |
| TAIWAN | EWT | country_equity | 2026-06-24 | -0.37% | 8.14% | 67.47% | 92.77% | 9.55% | 48.60% | -8.51% | 60.00% | -6.11% | 1.66 | pass |
| BRAZIL | EWZ | country_equity | 2026-06-24 | -0.76% | -6.04% | 8.68% | 26.41% | -4.63% | 20.81% | -7.67% | 30.00% | -18.11% | 1.03 | pass |
| MEXICO | EWW | country_equity | 2026-06-24 | -4.55% | -3.71% | 5.53% | 28.88% | -2.30% | 23.34% | -6.47% | 35.00% | -7.82% | 0.93 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-24 | -6.51% | -5.60% | -9.12% | 25.36% | -4.19% | 37.61% | -9.51% | 50.00% | -22.13% | 1.60 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-24 | 0.59% | 1.07% | 1.05% | 5.71% | 2.48% | 4.64% | -0.80% | 65.00% | -0.85% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-24 | 0.45% | 1.48% | 1.81% | 6.46% | 2.89% | 2.38% | -0.35% | 55.00% | -0.28% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-24 | 0.30% | 1.90% | 2.23% | 10.51% | 3.31% | 6.21% | -1.02% | 55.00% | -0.17% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-24 | 0.39% | 1.15% | 1.31% | 2.46% | 2.56% | 3.31% | -0.66% | 60.00% | -0.52% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-06-24 | -14.57% | -24.25% | -20.61% | 58.79% | -22.84% | 53.38% | -25.73% | 35.00% | -50.97% | 1.69 | pass |
| COPPER | CPER | commodities | 2026-06-24 | -6.03% | -6.71% | 6.17% | 18.31% | -5.30% | 33.89% | -10.57% | 50.00% | -10.57% | 1.26 | pass |
| AGRICULTURE | DBA | commodities | 2026-06-24 | -1.04% | -3.63% | 3.55% | 4.67% | -2.22% | 9.27% | -4.86% | 30.00% | -7.55% | 0.07 | pass |
| OIL | USO | commodities | 2026-06-24 | -6.95% | -24.57% | 51.41% | 45.60% | -23.16% | 43.03% | -24.54% | 30.00% | -30.51% | -1.03 | pass |
| US_DOLLAR | UUP | currencies | 2026-06-24 | 1.24% | 2.74% | 5.86% | 8.67% | 4.15% | 4.80% | -0.43% | 55.00% | 0.00% | -0.13 | pass |
| EURO | FXE | currencies | 2026-06-24 | -1.21% | -2.12% | -3.24% | -1.56% | -0.71% | 5.38% | -2.66% | 45.00% | -5.40% | 0.13 | pass |
| YEN | FXY | currencies | 2026-06-24 | -0.68% | -1.73% | -3.87% | -10.86% | -0.32% | 2.80% | -1.65% | 20.00% | -11.59% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-24 | -6.85% | -21.16% | -31.52% | -43.61% | -19.75% | 47.58% | -21.21% | 25.00% | -52.49% | 1.83 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-24 | -8.80% | -23.44% | -46.23% | -35.39% | -22.03% | 70.73% | -24.01% | 25.00% | -67.42% | 3.00 | pass |

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
