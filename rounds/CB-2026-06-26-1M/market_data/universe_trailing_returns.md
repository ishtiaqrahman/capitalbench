# Full-Universe Price, Risk, And Benchmark Context

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
