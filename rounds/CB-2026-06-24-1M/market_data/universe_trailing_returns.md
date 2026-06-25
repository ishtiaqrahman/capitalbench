# Full-Universe Price, Risk, And Benchmark Context

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
