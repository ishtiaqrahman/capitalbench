# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-15
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-15 | 0.00% | 0.00% | 0.00% | 0.00% | -0.25% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-15 | 0.08% | 0.30% | 1.77% | 3.82% | 0.05% | 0.25% | -0.01% | 75.00% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-15 | 1.26% | 0.25% | 9.62% | 22.67% | 0.00% | 12.59% | -3.17% | 45.00% | -0.37% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-15 | 1.13% | 0.26% | 9.53% | 23.09% | 0.00% | 11.86% | -2.49% | 45.00% | -0.23% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-15 | 0.89% | -3.42% | 15.71% | 29.54% | -3.68% | 26.21% | -4.93% | 45.00% | -3.70% | 1.38 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-15 | 1.46% | -0.63% | 5.21% | 15.42% | -0.88% | 21.45% | -5.03% | 50.00% | -3.95% | 1.25 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-15 | 0.85% | 1.44% | 13.60% | 29.46% | 1.18% | 11.10% | -1.39% | 60.00% | -0.19% | 0.73 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-15 | 1.20% | -0.70% | 8.19% | 22.55% | -0.95% | 12.55% | -3.09% | 50.00% | -1.92% | 1.00 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-15 | 0.78% | 0.38% | 11.86% | 36.57% | 0.13% | 13.26% | -2.32% | 50.00% | -1.56% | 1.26 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-15 | 1.66% | 1.84% | 13.93% | 39.35% | 1.58% | 10.48% | -1.83% | 50.00% | -0.20% | 1.02 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-15 | 0.00% | -0.10% | 13.24% | 24.78% | -0.35% | 12.42% | -2.36% | 50.00% | -0.71% | 0.28 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-15 | -0.51% | 1.90% | 4.47% | 7.14% | 1.65% | 14.80% | -1.89% | 55.00% | -1.89% | 0.04 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-15 | -0.69% | -6.28% | 21.81% | 32.74% | -6.54% | 42.77% | -9.50% | 55.00% | -9.43% | 1.50 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-15 | 0.10% | -5.21% | 25.14% | 41.55% | -5.47% | 34.29% | -6.75% | 50.00% | -8.28% | 1.68 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-15 | 3.58% | 1.32% | -1.87% | 8.32% | 1.07% | 20.17% | -5.76% | 55.00% | -5.03% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-15 | 1.47% | -1.13% | -4.26% | 7.65% | -1.38% | 20.44% | -4.21% | 50.00% | -5.66% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-15 | -1.09% | -1.67% | 2.61% | 7.14% | -1.93% | 18.34% | -3.32% | 50.00% | -6.10% | -0.05 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-15 | -2.47% | 3.99% | 1.71% | 21.46% | 3.73% | 21.71% | -3.74% | 55.00% | -3.74% | 0.34 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-15 | 2.89% | 5.97% | 4.93% | 11.21% | 5.72% | 14.71% | -2.08% | 65.00% | 0.00% | 0.65 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-15 | -0.20% | 1.02% | 9.19% | 21.68% | 0.77% | 17.75% | -2.96% | 60.00% | -2.96% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-15 | 1.62% | 2.44% | 20.31% | 34.12% | 2.19% | 21.60% | -4.25% | 45.00% | -9.04% | -0.20 | pass |
| MATERIALS | XLB | us_sector | 2026-07-15 | 0.68% | -3.45% | 3.99% | 15.37% | -3.70% | 17.48% | -4.50% | 50.00% | -5.05% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-15 | -0.31% | 1.72% | 5.08% | 13.38% | 1.46% | 15.85% | -3.10% | 55.00% | -3.99% | 0.16 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-15 | 0.93% | -0.09% | 8.52% | 11.59% | -0.34% | 17.91% | -2.75% | 60.00% | -1.50% | 0.30 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-15 | 0.29% | -0.20% | -0.71% | 3.76% | -0.46% | 5.26% | -1.54% | 60.00% | -2.74% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-15 | -0.14% | -1.36% | -2.45% | 3.61% | -1.62% | 9.21% | -3.62% | 50.00% | -5.50% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-15 | 0.02% | -0.58% | 0.65% | 3.45% | -0.83% | 4.26% | -0.85% | 55.00% | -0.90% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-15 | -0.08% | -0.95% | -0.78% | 4.52% | -1.20% | 5.02% | -2.16% | 55.00% | -1.88% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-15 | 0.19% | 0.17% | 1.44% | 5.98% | -0.08% | 2.76% | -0.44% | 40.00% | -0.08% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-15 | 0.10% | -0.39% | -0.12% | 4.45% | -0.64% | 4.10% | -1.34% | 60.00% | -1.60% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-15 | 0.68% | -1.65% | 9.78% | 29.27% | -1.91% | 18.30% | -3.63% | 60.00% | -2.17% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-15 | 0.52% | -2.12% | 5.70% | 22.05% | -2.37% | 19.81% | -4.34% | 50.00% | -2.87% | 1.09 | pass |
| EUROPE | VGK | international_equity | 2026-07-15 | 1.07% | 0.52% | 5.64% | 19.53% | 0.26% | 13.56% | -2.35% | 55.00% | -0.94% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-07-15 | 1.04% | -0.60% | 10.05% | 36.04% | -0.85% | 23.99% | -4.57% | 60.00% | -3.58% | 1.16 | pass |
| CHINA | MCHI | international_equity | 2026-07-15 | 2.46% | -1.42% | -14.28% | -2.66% | -1.67% | 20.52% | -8.10% | 45.00% | -17.64% | 0.94 | pass |
| INDIA | INDA | international_equity | 2026-07-15 | 0.14% | -1.10% | -8.46% | -11.22% | -1.35% | 13.38% | -2.54% | 50.00% | -11.88% | 0.62 | pass |
| GOLD | IAU | commodities | 2026-07-15 | -0.60% | -6.13% | -12.03% | 21.50% | -6.38% | 22.45% | -7.99% | 45.00% | -24.90% | 0.66 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-15 | 3.31% | 1.66% | 24.69% | 34.21% | 1.40% | 21.76% | -6.57% | 50.00% | -9.20% | -0.18 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-15 | -0.38% | -8.70% | 49.03% | 103.79% | -8.96% | 58.77% | -13.07% | 55.00% | -11.68% | 2.28 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-15 | 1.58% | 1.36% | -5.84% | -13.79% | 1.10% | 27.57% | -8.55% | 55.00% | -20.23% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-15 | -2.32% | -8.16% | 16.73% | 39.70% | -8.41% | 39.45% | -8.90% | 50.00% | -12.86% | 1.86 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-15 | -1.85% | -9.78% | -8.13% | 29.90% | -10.03% | 32.28% | -10.39% | 30.00% | -15.51% | 2.16 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-15 | 1.56% | 8.00% | 29.43% | 28.00% | 7.74% | 27.85% | -3.12% | 45.00% | -1.73% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-15 | 3.07% | -11.00% | 7.37% | 45.62% | -11.26% | 41.80% | -15.28% | 45.00% | -24.52% | 1.77 | pass |
| METALS_MINING | XME | commodities | 2026-07-15 | 1.24% | -14.39% | -16.47% | 43.30% | -14.65% | 26.53% | -15.44% | 35.00% | -22.25% | 1.69 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-15 | 0.36% | 0.43% | 7.59% | 18.92% | 0.17% | 10.64% | -1.83% | 50.00% | -0.94% | 0.73 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-15 | -4.14% | 14.64% | 25.75% | 82.67% | 14.39% | 27.73% | -5.44% | 70.00% | -4.91% | 1.01 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-15 | 3.33% | 5.53% | 12.35% | 26.48% | 5.27% | 18.38% | -3.73% | 70.00% | -0.53% | 0.82 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-15 | -1.34% | -0.41% | -1.85% | 22.98% | -0.67% | 19.37% | -6.27% | 60.00% | -5.73% | 1.02 | pass |
| CANADA | EWC | country_equity | 2026-07-15 | 2.62% | 0.95% | 8.24% | 30.98% | 0.70% | 9.45% | -3.08% | 70.00% | 0.00% | 0.77 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-15 | 0.60% | 1.21% | 5.21% | 22.14% | 0.96% | 14.40% | -2.28% | 40.00% | -2.55% | 0.72 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-15 | 2.42% | 0.70% | 9.59% | 13.94% | 0.44% | 13.92% | -4.42% | 55.00% | -3.49% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-15 | -6.06% | -18.83% | 54.56% | 140.17% | -19.08% | 78.44% | -23.35% | 45.00% | -21.70% | 2.65 | pass |
| TAIWAN | EWT | country_equity | 2026-07-15 | -1.36% | -3.65% | 52.31% | 83.97% | -3.90% | 43.66% | -8.65% | 55.00% | -8.11% | 1.71 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-15 | 4.27% | 3.58% | 8.58% | 36.48% | 3.32% | 19.56% | -2.63% | 40.00% | -13.20% | 1.01 | pass |
| MEXICO | EWW | country_equity | 2026-07-15 | 0.91% | -3.05% | 4.44% | 31.30% | -3.30% | 18.30% | -5.37% | 45.00% | -5.82% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-15 | 1.67% | -5.92% | -11.67% | 29.97% | -6.17% | 22.87% | -8.61% | 50.00% | -20.18% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-15 | 0.15% | -0.37% | 0.17% | 5.88% | -0.63% | 4.80% | -1.45% | 60.00% | -1.47% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-15 | -0.14% | -0.11% | 0.69% | 6.34% | -0.37% | 2.50% | -0.75% | 55.00% | -0.75% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-15 | -0.06% | -0.60% | 1.92% | 10.07% | -0.86% | 4.63% | -1.08% | 45.00% | -0.71% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-15 | 0.42% | -0.27% | 0.21% | 2.21% | -0.52% | 3.48% | -1.20% | 50.00% | -1.26% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-15 | -1.17% | -17.74% | -37.34% | 52.39% | -18.00% | 44.07% | -18.42% | 40.00% | -50.56% | 1.69 | pass |
| COPPER | CPER | commodities | 2026-07-15 | 4.21% | -2.57% | 5.06% | 12.59% | -2.83% | 24.77% | -8.42% | 50.00% | -4.85% | 1.23 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-15 | 1.30% | 6.07% | 9.34% | 13.15% | 5.81% | 14.41% | -1.52% | 60.00% | -2.61% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-15 | 8.17% | 0.14% | 70.65% | 61.28% | -0.11% | 50.60% | -14.80% | 50.00% | -20.65% | -1.03 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-15 | -0.39% | 1.00% | 2.99% | 6.47% | 0.75% | 5.58% | -0.98% | 50.00% | -0.98% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-15 | 0.34% | -0.94% | -0.76% | -0.44% | -1.20% | 5.66% | -2.19% | 45.00% | -4.40% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-15 | 0.12% | -1.24% | -2.47% | -8.60% | -1.50% | 5.38% | -1.42% | 35.00% | -10.06% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-15 | 4.48% | -2.46% | -31.83% | -44.36% | -2.72% | 38.49% | -11.79% | 55.00% | -48.37% | 1.81 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-15 | 10.76% | 5.52% | -41.52% | -37.01% | 5.27% | 51.83% | -14.68% | 50.00% | -60.32% | 2.97 | pass |
