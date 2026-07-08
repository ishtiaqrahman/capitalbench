# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-07
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-07 | 0.00% | 0.00% | 0.00% | 0.00% | -1.64% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-07 | 0.09% | 0.29% | 1.45% | 3.51% | -1.35% | 0.24% | -0.01% | 73.68% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-07 | 0.13% | 1.64% | 9.01% | 21.80% | 0.00% | 16.24% | -3.17% | 42.11% | -1.31% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-07 | -0.12% | 2.01% | 9.35% | 22.36% | 0.37% | 15.54% | -2.49% | 42.11% | -0.98% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-07 | -3.66% | 0.73% | 13.96% | 29.13% | -0.91% | 31.61% | -4.93% | 42.11% | -4.82% | 1.37 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-07 | -2.27% | -1.01% | 1.95% | 14.56% | -2.64% | 23.50% | -5.03% | 42.11% | -5.68% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-07 | 2.19% | 5.12% | 16.38% | 28.54% | 3.48% | 13.88% | -1.39% | 63.16% | 0.00% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-07 | -2.13% | 2.31% | 11.10% | 21.07% | 0.67% | 15.99% | -2.13% | 57.89% | -2.13% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-07 | -1.42% | 5.41% | 16.42% | 36.20% | 3.77% | 16.70% | -1.62% | 57.89% | -1.42% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-07 | -0.46% | 5.51% | 18.29% | 37.86% | 3.87% | 12.96% | -1.77% | 52.63% | -0.70% | 1.03 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-07 | 2.62% | 1.55% | 18.55% | 24.67% | -0.09% | 12.58% | -2.93% | 52.63% | -0.09% | 0.29 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-07 | 2.70% | 4.89% | 9.62% | 7.86% | 3.26% | 14.29% | -1.89% | 63.16% | 0.00% | 0.06 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-07 | -8.86% | 2.06% | 22.07% | 31.89% | 0.42% | 47.51% | -9.50% | 52.63% | -9.50% | 1.50 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-07 | -5.95% | -0.50% | 22.58% | 41.32% | -2.14% | 39.62% | -6.75% | 47.37% | -9.49% | 1.67 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-07 | 3.63% | -0.32% | -4.63% | 5.06% | -1.96% | 18.91% | -5.76% | 57.89% | -7.01% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-07 | 0.09% | 2.41% | -2.51% | 8.34% | 0.77% | 22.98% | -4.21% | 57.89% | -5.35% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-07 | 2.15% | 2.41% | 12.15% | 6.22% | 0.77% | 18.40% | -3.58% | 52.63% | -4.53% | -0.04 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-07 | 3.64% | 7.94% | 3.87% | 24.53% | 6.31% | 20.69% | -3.34% | 63.16% | 0.00% | 0.35 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-07 | 4.55% | 7.55% | 1.66% | 8.05% | 5.91% | 13.27% | -1.44% | 63.16% | -0.16% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-07 | -1.54% | 4.97% | 15.33% | 24.06% | 3.33% | 25.26% | -3.38% | 68.42% | -1.71% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-07 | 2.88% | -4.57% | 22.74% | 30.74% | -6.21% | 23.66% | -8.81% | 36.84% | -12.03% | -0.17 | pass |
| MATERIALS | XLB | us_sector | 2026-07-07 | 1.34% | 2.12% | 11.25% | 15.92% | 0.48% | 22.60% | -3.55% | 57.89% | -3.15% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-07 | 0.79% | 3.70% | 10.61% | 14.56% | 2.06% | 15.55% | -3.10% | 73.68% | -2.97% | 0.17 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-07 | 1.95% | 1.31% | 13.57% | 11.95% | -0.33% | 19.21% | -3.31% | 57.89% | -0.77% | 0.30 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-07 | -0.59% | 0.42% | -1.31% | 2.73% | -1.22% | 5.70% | -1.11% | 63.16% | -3.15% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-07 | -1.80% | -0.23% | -1.89% | 2.23% | -1.87% | 10.69% | -2.96% | 47.37% | -5.53% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-07 | -0.19% | -0.02% | -0.43% | 2.25% | -1.66% | 4.58% | -0.78% | 57.89% | -1.95% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-07 | -0.74% | 0.08% | -0.58% | 3.69% | -1.56% | 5.73% | -1.31% | 52.63% | -1.98% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-07 | 0.20% | 0.88% | 1.06% | 5.04% | -0.76% | 3.35% | -0.39% | 42.11% | -0.22% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-07 | -0.45% | 0.38% | -0.28% | 3.78% | -1.26% | 4.36% | -0.84% | 63.16% | -1.86% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-07 | -0.66% | 2.87% | 11.57% | 28.87% | 1.23% | 22.65% | -3.07% | 57.89% | -2.22% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-07 | -1.36% | 1.59% | 6.70% | 22.23% | -0.05% | 22.83% | -4.34% | 47.37% | -3.85% | 1.08 | pass |
| EUROPE | VGK | international_equity | 2026-07-07 | 0.56% | 3.58% | 6.44% | 18.88% | 1.95% | 17.90% | -2.08% | 57.89% | -1.03% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-07-07 | -0.21% | 3.15% | 12.85% | 33.31% | 1.51% | 27.59% | -4.50% | 63.16% | -4.02% | 1.15 | pass |
| CHINA | MCHI | international_equity | 2026-07-07 | 1.47% | -4.26% | -15.77% | -3.40% | -5.89% | 17.88% | -8.10% | 47.37% | -21.24% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-07 | -0.12% | 4.20% | -8.99% | -10.89% | 2.56% | 14.69% | -1.70% | 63.16% | -11.42% | 0.61 | pass |
| GOLD | IAU | commodities | 2026-07-07 | 2.46% | -4.74% | -7.68% | 22.97% | -6.38% | 29.89% | -7.99% | 47.37% | -23.83% | 0.64 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-07 | 2.77% | -6.53% | 21.70% | 27.57% | -8.17% | 18.34% | -10.44% | 31.58% | -13.70% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-07 | -11.35% | 2.06% | 51.02% | 108.49% | 0.43% | 65.61% | -13.07% | 52.63% | -13.07% | 2.26 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-07 | 3.90% | -1.78% | -11.38% | -14.96% | -3.41% | 29.91% | -11.37% | 42.11% | -20.07% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-07 | -5.38% | -0.70% | 18.07% | 42.71% | -2.34% | 45.26% | -7.81% | 52.63% | -11.49% | 1.85 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-07 | -5.91% | -4.00% | -0.36% | 41.46% | -5.64% | 42.37% | -8.23% | 31.58% | -13.50% | 2.15 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-07 | 2.63% | 6.45% | 25.87% | 22.50% | 4.81% | 25.28% | -3.34% | 47.37% | -2.15% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-07 | -7.34% | -14.43% | 8.60% | 42.18% | -16.06% | 46.24% | -13.79% | 36.84% | -25.86% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-07-07 | -4.17% | -13.54% | -10.13% | 48.68% | -15.18% | 35.19% | -15.00% | 36.84% | -22.80% | 1.69 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-07 | 0.92% | 3.72% | 11.14% | 18.83% | 2.08% | 12.67% | -1.83% | 63.16% | -0.13% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-07 | 3.55% | 27.48% | 29.74% | 96.96% | 25.84% | 23.98% | -1.93% | 78.95% | 0.00% | 1.04 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-07 | 0.29% | 7.61% | 13.78% | 22.87% | 5.97% | 17.55% | -3.08% | 73.68% | -1.46% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-07 | 1.11% | 6.90% | 8.41% | 30.99% | 5.26% | 27.22% | -3.00% | 68.42% | -2.26% | 1.01 | pass |
| CANADA | EWC | country_equity | 2026-07-07 | 1.25% | 1.04% | 8.56% | 28.10% | -0.60% | 10.32% | -3.08% | 63.16% | -1.39% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-07 | 2.15% | 3.07% | 7.45% | 23.61% | 1.43% | 16.48% | -2.28% | 42.11% | -1.80% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-07 | -0.11% | 1.66% | 8.59% | 11.67% | 0.02% | 17.26% | -4.42% | 52.63% | -5.73% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-07 | -10.21% | 3.48% | 69.38% | 164.54% | 1.84% | 88.72% | -17.82% | 42.11% | -17.29% | 2.62 | pass |
| TAIWAN | EWT | country_equity | 2026-07-07 | -6.20% | 3.87% | 55.33% | 84.90% | 2.24% | 47.71% | -8.65% | 57.89% | -8.65% | 1.70 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-07 | 0.41% | 2.82% | 6.94% | 26.56% | 1.18% | 17.98% | -2.99% | 42.11% | -16.20% | 0.98 | pass |
| MEXICO | EWW | country_equity | 2026-07-07 | -0.31% | 1.39% | 8.90% | 26.99% | -0.25% | 23.35% | -5.37% | 47.37% | -6.26% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-07 | 0.63% | 0.95% | -9.05% | 27.30% | -0.69% | 33.42% | -8.61% | 52.63% | -20.36% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-07 | -0.36% | 0.46% | 0.18% | 5.16% | -1.17% | 4.90% | -0.84% | 68.42% | -1.80% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-07 | -0.08% | 0.52% | 0.96% | 5.89% | -1.12% | 2.44% | -0.31% | 57.89% | -0.48% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-07 | -0.10% | 0.98% | 1.96% | 9.25% | -0.65% | 5.78% | -0.50% | 47.37% | -0.50% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-07 | -0.62% | 0.25% | 0.08% | 1.56% | -1.39% | 3.33% | -0.80% | 52.63% | -1.51% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-07 | 1.85% | -11.55% | -23.25% | 62.91% | -13.19% | 51.56% | -18.42% | 47.37% | -48.43% | 1.65 | pass |
| COPPER | CPER | commodities | 2026-07-07 | -0.90% | -1.81% | 4.12% | 20.03% | -3.45% | 28.31% | -8.42% | 52.63% | -7.91% | 1.23 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-07 | 3.30% | 4.36% | 6.33% | 11.02% | 2.72% | 14.39% | -1.52% | 52.63% | -4.11% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-07 | 2.33% | -18.12% | 60.67% | 42.42% | -19.76% | 42.02% | -23.59% | 36.84% | -28.79% | -0.98 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-07 | -0.04% | 1.36% | 4.41% | 8.50% | -0.28% | 5.14% | -0.74% | 52.63% | -0.46% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-07 | -0.06% | -0.86% | -1.97% | -1.97% | -2.49% | 5.45% | -2.19% | 52.63% | -4.91% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-07 | 0.34% | -1.19% | -3.36% | -10.25% | -2.83% | 5.18% | -1.74% | 26.32% | -10.25% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-07 | 8.59% | 5.89% | -29.86% | -41.12% | 4.25% | 39.68% | -11.79% | 47.37% | -49.29% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-07 | 13.62% | 13.82% | -42.95% | -29.85% | 12.18% | 59.24% | -14.68% | 42.11% | -63.08% | 2.95 | pass |
