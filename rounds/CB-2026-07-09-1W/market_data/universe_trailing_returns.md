# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-09
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-09 | 0.00% | 0.00% | 0.00% | 0.00% | -2.25% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-09 | 0.02% | 0.29% | 1.44% | 3.51% | -1.96% | 0.24% | -0.01% | 75.00% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-09 | 0.93% | 2.25% | 8.88% | 21.79% | 0.00% | 16.05% | -3.17% | 45.00% | -0.78% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-09 | 0.73% | 2.43% | 9.14% | 22.21% | 0.18% | 15.42% | -2.49% | 45.00% | -0.49% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-09 | 1.50% | 2.30% | 15.69% | 30.65% | 0.04% | 31.02% | -4.93% | 50.00% | -2.96% | 1.37 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-09 | 1.77% | 1.14% | 3.76% | 15.44% | -1.11% | 23.16% | -5.03% | 50.00% | -4.16% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-09 | -0.17% | 3.77% | 14.02% | 27.59% | 1.52% | 14.27% | -1.39% | 60.00% | -0.55% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-09 | -0.51% | 1.55% | 10.06% | 20.49% | -0.70% | 16.42% | -3.09% | 55.00% | -1.83% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-09 | -0.11% | 4.54% | 14.70% | 34.28% | 2.28% | 17.21% | -2.32% | 55.00% | -1.07% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-09 | -0.83% | 3.83% | 15.58% | 35.14% | 1.58% | 13.71% | -1.83% | 50.00% | -1.01% | 1.04 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-09 | -0.40% | 0.39% | 14.86% | 22.55% | -1.86% | 12.50% | -2.93% | 45.00% | -0.95% | 0.30 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-09 | -1.60% | 2.72% | 6.27% | 6.21% | 0.47% | 14.46% | -1.89% | 55.00% | -1.85% | 0.06 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-09 | 1.48% | 3.18% | 25.24% | 35.98% | 0.93% | 46.62% | -9.50% | 60.00% | -6.96% | 1.50 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-09 | 2.64% | 2.66% | 27.13% | 44.53% | 0.40% | 39.00% | -6.75% | 55.00% | -6.38% | 1.67 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-09 | 0.83% | -0.61% | -5.73% | 4.52% | -2.86% | 19.38% | -5.76% | 55.00% | -7.44% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-09 | -0.23% | 1.05% | -5.70% | 7.57% | -1.21% | 23.79% | -4.21% | 55.00% | -5.78% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-09 | -2.11% | -0.38% | 6.31% | 5.80% | -2.64% | 18.35% | -3.58% | 45.00% | -6.40% | -0.04 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-09 | -0.96% | 5.38% | 3.97% | 21.78% | 3.13% | 20.81% | -3.34% | 55.00% | -1.38% | 0.35 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-09 | -0.14% | 6.24% | 0.52% | 7.64% | 3.99% | 15.43% | -2.08% | 60.00% | -1.07% | 0.67 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-09 | -1.52% | 3.39% | 12.43% | 22.38% | 1.14% | 24.83% | -3.38% | 65.00% | -2.40% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-09 | 3.01% | -3.79% | 19.08% | 28.39% | -6.04% | 24.00% | -8.69% | 40.00% | -11.74% | -0.18 | pass |
| MATERIALS | XLB | us_sector | 2026-07-09 | -3.36% | -0.63% | 5.00% | 11.52% | -2.89% | 23.44% | -4.50% | 55.00% | -5.50% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-09 | -1.38% | 3.27% | 7.59% | 13.28% | 1.02% | 15.48% | -3.10% | 65.00% | -4.18% | 0.17 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-09 | -1.01% | -0.78% | 10.91% | 10.52% | -3.04% | 18.20% | -3.31% | 55.00% | -2.23% | 0.31 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-09 | -0.44% | 0.26% | -1.11% | 2.36% | -2.00% | 5.57% | -1.31% | 60.00% | -3.14% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-09 | -1.19% | -0.37% | -2.12% | 1.22% | -2.63% | 10.23% | -3.18% | 45.00% | -5.59% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-09 | -0.19% | -0.13% | -0.41% | 1.91% | -2.38% | 4.44% | -0.78% | 55.00% | -2.00% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-09 | -0.86% | -0.30% | -0.82% | 3.23% | -2.55% | 5.49% | -1.51% | 50.00% | -2.14% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-09 | 0.05% | 0.63% | 0.90% | 4.89% | -1.62% | 3.32% | -0.39% | 40.00% | -0.24% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-09 | -0.44% | 0.14% | -0.35% | 3.36% | -2.11% | 4.27% | -1.01% | 60.00% | -1.89% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-09 | -0.11% | 1.81% | 10.37% | 26.99% | -0.44% | 22.26% | -3.07% | 60.00% | -2.29% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-09 | 0.76% | 1.90% | 7.45% | 23.05% | -0.35% | 22.33% | -4.34% | 50.00% | -2.86% | 1.08 | pass |
| EUROPE | VGK | international_equity | 2026-07-09 | -1.05% | 1.97% | 4.97% | 15.80% | -0.28% | 17.85% | -2.08% | 55.00% | -1.73% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-07-09 | 0.41% | 3.38% | 11.13% | 33.08% | 1.13% | 26.81% | -4.57% | 65.00% | -3.56% | 1.16 | pass |
| CHINA | MCHI | international_equity | 2026-07-09 | 4.48% | -1.39% | -13.95% | -0.70% | -3.65% | 19.11% | -8.10% | 50.00% | -19.10% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-09 | -1.09% | 3.11% | -7.82% | -11.93% | 0.86% | 15.43% | -2.54% | 60.00% | -11.93% | 0.61 | pass |
| GOLD | IAU | commodities | 2026-07-09 | 0.00% | -3.20% | -8.69% | 23.98% | -5.45% | 29.05% | -7.99% | 50.00% | -23.69% | 0.64 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-09 | 3.47% | -5.52% | 21.09% | 28.16% | -7.78% | 19.42% | -9.47% | 35.00% | -13.17% | -0.17 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-09 | 2.61% | 2.83% | 56.14% | 113.59% | 0.58% | 64.67% | -13.07% | 60.00% | -9.15% | 2.26 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-09 | 0.33% | 1.02% | -10.57% | -15.73% | -1.23% | 28.51% | -8.79% | 45.00% | -20.28% | 1.19 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-09 | 3.20% | 1.06% | 21.40% | 45.96% | -1.19% | 44.21% | -7.81% | 60.00% | -9.00% | 1.86 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-09 | -2.53% | -3.24% | -3.51% | 40.13% | -5.49% | 40.78% | -8.23% | 35.00% | -13.29% | 2.15 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-09 | 3.96% | 11.86% | 30.26% | 24.17% | 9.61% | 24.66% | -3.12% | 50.00% | 0.00% | 1.11 | pass |
| SOLAR | TAN | clean_energy | 2026-07-09 | -2.43% | -11.13% | 9.24% | 42.43% | -13.38% | 45.07% | -14.10% | 40.00% | -25.67% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-07-09 | -1.80% | -11.02% | -11.57% | 51.29% | -13.27% | 34.56% | -15.44% | 40.00% | -22.22% | 1.69 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-09 | -0.66% | 2.46% | 8.93% | 17.50% | 0.20% | 13.19% | -1.83% | 60.00% | -0.70% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-09 | 2.38% | 25.16% | 32.08% | 87.81% | 22.91% | 23.94% | -1.93% | 75.00% | 0.00% | 1.03 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-09 | -0.49% | 5.40% | 11.92% | 21.14% | 3.15% | 20.01% | -3.73% | 70.00% | -2.01% | 0.84 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-09 | -3.45% | 4.05% | 2.99% | 27.49% | 1.80% | 27.81% | -4.45% | 60.00% | -4.45% | 1.01 | pass |
| CANADA | EWC | country_equity | 2026-07-09 | 1.06% | 1.08% | 7.37% | 28.28% | -1.18% | 10.64% | -3.08% | 65.00% | -1.35% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-09 | -1.59% | 1.72% | 5.10% | 19.93% | -0.53% | 16.88% | -2.28% | 40.00% | -3.30% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-09 | 0.39% | 1.23% | 8.90% | 10.84% | -1.03% | 16.69% | -4.42% | 50.00% | -5.50% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-09 | 2.56% | 0.38% | 69.67% | 162.07% | -1.87% | 86.40% | -17.82% | 50.00% | -15.72% | 2.62 | pass |
| TAIWAN | EWT | country_equity | 2026-07-09 | 0.18% | 4.22% | 59.36% | 89.34% | 1.96% | 47.01% | -8.65% | 60.00% | -5.81% | 1.69 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-09 | 1.54% | 4.05% | 6.75% | 29.72% | 1.80% | 18.41% | -2.99% | 40.00% | -15.43% | 0.99 | pass |
| MEXICO | EWW | country_equity | 2026-07-09 | -1.67% | 0.77% | 6.01% | 27.37% | -1.49% | 22.93% | -5.37% | 45.00% | -7.26% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-09 | -1.13% | -0.65% | -8.52% | 26.31% | -2.90% | 33.08% | -8.61% | 50.00% | -20.75% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-09 | -0.33% | 0.28% | -0.34% | 4.56% | -1.97% | 4.79% | -0.99% | 65.00% | -1.82% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-09 | -0.52% | 0.18% | 0.66% | 5.62% | -2.08% | 2.64% | -0.61% | 55.00% | -0.76% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-09 | -0.25% | 0.72% | 1.77% | 8.85% | -1.53% | 5.54% | -0.65% | 45.00% | -0.48% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-09 | -0.46% | 0.29% | 0.06% | 1.62% | -1.96% | 3.83% | -1.20% | 50.00% | -1.51% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-09 | -1.60% | -8.25% | -25.20% | 64.06% | -10.50% | 50.38% | -18.42% | 50.00% | -48.73% | 1.67 | pass |
| COPPER | CPER | commodities | 2026-07-09 | 1.23% | -2.20% | 4.43% | 10.06% | -4.45% | 28.57% | -8.42% | 50.00% | -7.02% | 1.24 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-09 | 3.63% | 5.44% | 7.49% | 10.72% | 3.19% | 13.92% | -1.52% | 60.00% | -3.55% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-09 | 4.84% | -16.98% | 54.01% | 41.70% | -19.23% | 43.43% | -23.10% | 40.00% | -28.73% | -1.00 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-09 | 0.07% | 1.25% | 3.77% | 8.26% | -1.00% | 5.04% | -0.74% | 50.00% | -0.60% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-09 | -0.05% | -0.98% | -1.50% | -1.89% | -3.23% | 5.32% | -2.19% | 50.00% | -4.81% | 0.12 | pass |
| YEN | FXY | currencies | 2026-07-09 | -0.83% | -1.31% | -3.01% | -10.25% | -3.56% | 5.13% | -1.74% | 30.00% | -10.28% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-09 | 2.70% | 1.91% | -30.00% | -43.68% | -0.35% | 39.40% | -11.79% | 50.00% | -49.77% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-09 | 2.57% | 5.69% | -43.12% | -37.10% | 3.44% | 58.35% | -14.68% | 45.00% | -63.95% | 2.93 | pass |
