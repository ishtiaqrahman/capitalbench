# Full-Universe Price, Risk, And Benchmark Context

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
