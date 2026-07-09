# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-08
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-08 | 0.00% | 0.00% | 0.00% | 0.00% | -1.10% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-08 | 0.05% | 0.28% | 1.45% | 3.51% | -0.81% | 0.24% | -0.01% | 70.00% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-08 | -0.05% | 1.10% | 8.68% | 21.49% | 0.00% | 15.87% | -3.17% | 40.00% | -1.61% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-08 | -0.28% | 1.33% | 8.92% | 21.92% | 0.23% | 15.21% | -2.49% | 40.00% | -1.35% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-08 | -1.89% | -0.54% | 14.93% | 29.43% | -1.63% | 30.78% | -4.93% | 45.00% | -4.55% | 1.37 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-08 | -0.99% | -0.87% | 3.12% | 15.08% | -1.97% | 22.92% | -5.03% | 45.00% | -5.33% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-08 | 0.54% | 3.67% | 14.24% | 27.33% | 2.57% | 14.24% | -1.39% | 60.00% | -1.03% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-08 | -2.24% | 1.09% | 9.61% | 19.39% | -0.01% | 16.04% | -3.09% | 55.00% | -3.09% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-08 | -1.95% | 3.54% | 14.11% | 34.02% | 2.45% | 16.76% | -2.32% | 55.00% | -2.32% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-08 | -1.82% | 3.42% | 15.32% | 35.05% | 2.32% | 13.53% | -1.83% | 50.00% | -1.83% | 1.04 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-08 | 1.54% | 0.95% | 15.67% | 22.72% | -0.14% | 12.49% | -2.93% | 50.00% | -0.71% | 0.30 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-08 | 0.82% | 4.88% | 6.77% | 6.86% | 3.78% | 15.17% | -1.89% | 60.00% | -1.38% | 0.06 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-08 | -4.04% | 0.04% | 24.53% | 34.11% | -1.06% | 46.32% | -9.50% | 55.00% | -8.80% | 1.50 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-08 | -2.27% | -1.39% | 26.07% | 42.30% | -2.49% | 38.86% | -6.75% | 50.00% | -8.37% | 1.66 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-08 | -0.26% | -1.21% | -6.29% | 3.80% | -2.31% | 19.09% | -5.76% | 55.00% | -8.32% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-08 | -2.36% | 0.12% | -5.82% | 6.77% | -0.97% | 23.35% | -4.21% | 55.00% | -7.03% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-08 | 1.31% | 2.29% | 8.94% | 6.61% | 1.20% | 18.08% | -3.58% | 50.00% | -5.06% | -0.04 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-08 | 1.73% | 6.79% | 3.52% | 22.35% | 5.69% | 21.05% | -3.34% | 60.00% | -1.30% | 0.36 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-08 | 0.35% | 6.14% | -0.81% | 6.92% | 5.05% | 15.37% | -2.08% | 60.00% | -2.08% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-08 | -1.60% | 4.17% | 13.24% | 22.76% | 3.07% | 25.05% | -3.38% | 65.00% | -2.77% | 0.98 | pass |
| ENERGY | XLE | us_sector | 2026-07-08 | 5.28% | -3.99% | 21.09% | 29.55% | -5.09% | 24.15% | -8.81% | 40.00% | -10.48% | -0.17 | pass |
| MATERIALS | XLB | us_sector | 2026-07-08 | -1.69% | 0.78% | 6.47% | 11.97% | -0.32% | 24.15% | -4.50% | 55.00% | -5.69% | 0.78 | pass |
| UTILITIES | XLU | us_sector | 2026-07-08 | 1.32% | 4.89% | 9.48% | 14.92% | 3.80% | 15.58% | -3.10% | 70.00% | -3.69% | 0.17 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-08 | -0.07% | 1.15% | 10.87% | 10.27% | 0.06% | 19.76% | -3.31% | 55.00% | -2.41% | 0.30 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-08 | -0.55% | 0.32% | -1.21% | 2.67% | -0.78% | 5.60% | -1.31% | 60.00% | -3.34% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-08 | -1.36% | 0.06% | -1.62% | 2.13% | -1.03% | 10.44% | -3.18% | 45.00% | -5.74% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-08 | -0.11% | -0.02% | -0.34% | 2.22% | -1.12% | 4.48% | -0.78% | 55.00% | -2.06% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-08 | -0.73% | -0.01% | -0.49% | 3.79% | -1.11% | 5.62% | -1.51% | 50.00% | -2.17% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-08 | 0.09% | 0.62% | 0.86% | 5.06% | -0.48% | 3.31% | -0.39% | 40.00% | -0.35% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-08 | -0.47% | 0.20% | -0.27% | 3.64% | -0.89% | 4.30% | -1.01% | 60.00% | -2.03% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-08 | -0.03% | 1.22% | 10.78% | 27.15% | 0.12% | 22.20% | -3.07% | 55.00% | -2.83% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-08 | -0.08% | 1.56% | 7.11% | 22.37% | 0.46% | 22.27% | -4.34% | 50.00% | -3.38% | 1.08 | pass |
| EUROPE | VGK | international_equity | 2026-07-08 | 0.47% | 2.13% | 5.42% | 16.61% | 1.03% | 17.88% | -2.08% | 55.00% | -1.99% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-07-08 | -0.55% | 1.19% | 12.29% | 31.88% | 0.09% | 26.96% | -4.57% | 60.00% | -4.57% | 1.15 | pass |
| CHINA | MCHI | international_equity | 2026-07-08 | 2.56% | -1.35% | -14.58% | -2.32% | -2.45% | 19.13% | -8.10% | 50.00% | -19.61% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-08 | -1.14% | 3.05% | -9.44% | -12.64% | 1.95% | 15.40% | -2.54% | 60.00% | -12.64% | 0.61 | pass |
| GOLD | IAU | commodities | 2026-07-08 | 1.03% | -5.70% | -8.95% | 23.26% | -6.80% | 29.16% | -7.99% | 45.00% | -24.45% | 0.64 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-08 | 5.32% | -5.68% | 22.57% | 29.62% | -6.77% | 19.53% | -10.44% | 35.00% | -12.11% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-08 | -4.43% | -0.86% | 56.47% | 109.84% | -1.96% | 64.28% | -13.07% | 55.00% | -11.35% | 2.26 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-08 | -0.92% | -3.30% | -11.43% | -16.73% | -4.39% | 29.72% | -11.37% | 40.00% | -21.47% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-08 | -1.67% | -2.90% | 20.00% | 43.37% | -4.00% | 44.18% | -7.81% | 55.00% | -10.79% | 1.85 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-08 | -5.08% | -5.98% | -2.42% | 40.31% | -7.07% | 41.25% | -8.23% | 30.00% | -13.91% | 2.15 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-08 | 0.60% | 6.51% | 26.97% | 21.77% | 5.42% | 24.85% | -3.34% | 45.00% | -2.74% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-08 | -6.33% | -14.85% | 7.42% | 42.17% | -15.94% | 45.04% | -14.85% | 35.00% | -26.77% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-07-08 | -2.32% | -13.98% | -10.49% | 49.10% | -15.08% | 34.26% | -15.44% | 35.00% | -23.20% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-08 | -0.57% | 2.61% | 8.89% | 17.14% | 1.51% | 13.27% | -1.83% | 60.00% | -1.30% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-08 | 4.10% | 27.02% | 31.86% | 93.27% | 25.92% | 24.25% | -1.93% | 75.00% | -0.55% | 1.04 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-08 | -3.73% | 4.84% | 8.99% | 18.96% | 3.75% | 19.56% | -3.73% | 70.00% | -3.73% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-08 | -1.73% | 5.52% | 5.51% | 28.96% | 4.42% | 28.11% | -4.45% | 65.00% | -4.45% | 1.02 | pass |
| CANADA | EWC | country_equity | 2026-07-08 | 0.52% | 0.31% | 6.95% | 27.74% | -0.78% | 10.37% | -3.08% | 60.00% | -2.05% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-08 | 1.20% | 1.56% | 5.73% | 20.80% | 0.47% | 16.92% | -2.28% | 40.00% | -3.13% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-08 | 1.52% | 1.59% | 8.14% | 10.95% | 0.49% | 16.80% | -4.42% | 50.00% | -5.77% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-08 | -1.50% | -1.57% | 71.42% | 159.19% | -2.67% | 86.40% | -17.82% | 45.00% | -16.64% | 2.62 | pass |
| TAIWAN | EWT | country_equity | 2026-07-08 | -1.69% | 3.46% | 58.77% | 88.47% | 2.36% | 46.90% | -8.65% | 60.00% | -6.84% | 1.69 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-08 | 0.67% | 3.11% | 5.65% | 25.23% | 2.01% | 17.77% | -2.99% | 40.00% | -16.76% | 0.98 | pass |
| MEXICO | EWW | country_equity | 2026-07-08 | -0.74% | 1.21% | 7.56% | 26.89% | 0.12% | 22.81% | -5.37% | 45.00% | -6.67% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-08 | -0.06% | -1.18% | -8.92% | 25.57% | -2.28% | 32.93% | -8.61% | 50.00% | -21.49% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-08 | -0.35% | 0.35% | 0.12% | 4.93% | -0.75% | 4.82% | -0.99% | 65.00% | -1.96% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-08 | -0.40% | 0.24% | 0.76% | 5.72% | -0.85% | 2.66% | -0.61% | 55.00% | -0.79% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-08 | -0.24% | 0.95% | 1.96% | 9.42% | -0.14% | 5.68% | -0.65% | 45.00% | -0.65% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-08 | -0.91% | -0.02% | -0.32% | 1.40% | -1.12% | 3.56% | -1.20% | 50.00% | -1.90% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-08 | -1.40% | -14.21% | -24.21% | 58.70% | -15.30% | 50.90% | -18.42% | 45.00% | -49.97% | 1.66 | pass |
| COPPER | CPER | commodities | 2026-07-08 | -0.38% | -3.84% | 3.90% | 9.77% | -4.93% | 27.67% | -8.42% | 50.00% | -8.69% | 1.23 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-08 | 2.83% | 4.90% | 6.19% | 11.17% | 3.80% | 14.01% | -1.52% | 55.00% | -3.86% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-08 | 8.66% | -16.97% | 59.07% | 45.80% | -18.07% | 43.43% | -23.59% | 40.00% | -26.64% | -0.99 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-08 | -0.46% | 1.18% | 4.00% | 8.26% | 0.08% | 5.06% | -0.74% | 50.00% | -0.60% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-08 | 0.48% | -0.85% | -1.59% | -1.90% | -1.94% | 5.35% | -2.19% | 55.00% | -4.78% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-08 | 0.05% | -1.43% | -3.52% | -10.12% | -2.53% | 5.12% | -1.74% | 25.00% | -10.31% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-08 | 3.62% | -1.84% | -31.62% | -43.01% | -2.93% | 39.72% | -11.79% | 45.00% | -50.58% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-08 | 7.55% | 3.07% | -44.09% | -33.72% | 1.97% | 58.87% | -14.68% | 40.00% | -64.17% | 2.95 | pass |
