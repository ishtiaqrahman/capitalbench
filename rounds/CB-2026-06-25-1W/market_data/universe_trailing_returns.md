# Full-Universe Price, Risk, And Benchmark Context

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
