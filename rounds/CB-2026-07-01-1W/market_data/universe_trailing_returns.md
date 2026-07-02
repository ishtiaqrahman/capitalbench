# Full-Universe Price, Risk, And Benchmark Context

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
